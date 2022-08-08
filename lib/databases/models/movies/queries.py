
movie_queries = {}
movie_queries['find_movie_by_title'] = "SELECT * FROM movie WHERE id = 1 AND title = %s"
movie_queries['save_movie'] = "INSERT INTO movie (title, img, app_id, url) VALUES (%s, %s, %s, %s)"
