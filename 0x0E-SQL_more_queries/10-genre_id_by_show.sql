-- Import the database dump from hbtn_0d_tvshows to your MySQL server
-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- 0)echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p (it was at the begining of the project)
-- 1) bring the file to the repo
-- 2) mysql -u root -p hbtn_0d_tvshows < hbtn_0d_tvshows.sql (it was in the documentation)

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
