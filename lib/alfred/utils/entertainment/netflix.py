import json
from time import sleep
import webbrowser as web
from selenium import webdriver
from selenium.webdriver.common.by import By
from decouple import config


def netflix(bot, query):
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
    sleep(1.5)
    movies = []
    for i in range(0, 60):
        try:
            res = driver.find_element(By.ID,
                                      f'row-{i}')
            if res:
                movie = res.find_element(By.CLASS_NAME,
                                         'slider-refocus')
                movies.append(
                    {'title': movie.text, 'link_to_watch': movie.get_attribute('href')})
            else:
                continue
        except:
            continue
    sleep(1.5)
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
            bot.speak('Printing what i found to the screen for you sir')
            print(json.dumps(movies, indent=2))
    else:
        bot.speak('Printing what i found to the screen for you sir')
        print(json.dumps(movies, indent=2))
