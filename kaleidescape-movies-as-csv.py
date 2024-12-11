import requests
import csv
import json

def fetch_all_movie_data(base_url, store_prod_session_id):
    """
    Fetches movie data from all pages of the provided URL, including a cookie in the request.

    Args:
      base_url: The base URL of the API endpoint.
      store_prod_session_id: The value of the STORE_PROD_SESSION_ID cookie.

    Returns:
      A list of dictionaries, where each dictionary represents a movie with 'title' and 'media_quality'.
    """
    all_movies = []
    current_page = 1
    total_pages = 1  # Initialize to 1 to ensure at least one request
    cookies = {'STORE_PROD_SESSION_ID': store_prod_session_id}
    while current_page <= total_pages:
        url = f"{base_url}?page={current_page}"
        try:
            response = requests.get(url, cookies=cookies)
            response.raise_for_status()
            data = response.json()
            total_pages = data['num_pages']
            for package in data['packages']:
                all_movies.append({
                    'title': package['title'],
                    'media_quality': package['media_quality']
                })
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            break
        current_page += 1
    return all_movies

def write_to_csv(data, filename='kaleidescape-library.csv'):
    """
    Writes data to a CSV file.

    Args:
      data: A list of dictionaries to write to the CSV.
      filename: The name of the CSV file (default: 'output.csv').
    """
    with open(filename, 'w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['title', 'media_quality']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    base_url = "https://www.kaleidescape.com/movie-store/rest/packages/my/movies"
    store_prod_session_id = input("Enter the STORE_PROD_SESSION_ID cookie value: ") 
    all_movies = fetch_all_movie_data(base_url, store_prod_session_id)
    write_to_csv(all_movies)