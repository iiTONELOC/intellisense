import json
from time import sleep
import webbrowser as web
from selenium import webdriver
from selenium.webdriver.common.by import By
from decouple import config


def write_results(results):
    UI_FOLDER = config('UI_FOLDER')
    with open(UI_FOLDER+'\\movies\\search_results.js', 'w') as f:
        f.write('const data =' + results)


def show_movies(results, bot):
    bot.speak('Printing what I found to the screen for you sir')
    write_results(json.dumps(results, indent=2))
    sleep(.5)
    # open the HTML file that we created
    web.open(config('UI_FOLDER')+'\\movies\\index.html')


def netflix(bot, query):
    movies = []
    driver = webdriver.Edge(executable_path=config('EDGE_DRIVER'))
    driver.get('https://www.netflix.com/')
    log_in_btn = driver.find_element_by_class_name("authLinks")
    log_in_btn.click()
    sleep(1)
    user_name_field = driver.find_element_by_id(
        "id_userLoginId")
    pass_field = driver.find_element_by_id(
        "id_password")
    sleep(1)
    user_name_field.send_keys(config('N_FLIX'))
    sleep(1)
    pass_field.send_keys(config('N_FLIX_PASS'))
    sleep(1)
    driver.find_element_by_class_name("login-button").click()
    sleep(2.5)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[4]/div/a').click()
    sleep(3.5)
    driver.find_element_by_class_name(
        'icon-search').click()
    driver.find_element_by_id('searchInput').send_keys(
        query.split('netflix')[1])
    sleep(2.5)

    for i in range(0, 60):
        try:
            res = driver.find_element(By.ID,
                                      f'row-{i}')
            if res:
                movie = res.find_element(By.CLASS_NAME,
                                         'slider-refocus')
                # get image
                img_div = movie.find_element(By.CLASS_NAME, 'boxart-container')
                movie_img_src = img_div.find_element(
                    By.TAG_NAME, 'img').get_attribute('src')
                movies.append(
                    {'title': movie.text,
                     'img': movie_img_src,
                     'link_to_watch': movie.get_attribute('href')
                     }
                )
            else:
                continue
        except:
            continue
    # loop over our movies and see if we can find one to match our query
    exact_match = None
    for movie in movies:
        if movie['title'].lower().strip() == query.split('netflix')[1].lower().strip():
            exact_match = movie

    if exact_match is not None:
        bot.read([
            'Sir I found a movie that matches your query', exact_match[
                'title'], 'Would you like to watch it?'
        ])
        user_input = bot.take_user_input()
        if 'yes' in user_input:
            bot.speak('Opening Netflix')
            web.open(exact_match['link_to_watch'])
            bot.speak('Enjoy the movie')
        else:
            show_movies(movies, bot)
    else:
        show_movies(movies, bot)
