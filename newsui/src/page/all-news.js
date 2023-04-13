
import React, { useEffect, useState } from 'react';

function AllNews() {
  const [allNews, setAllNews] = useState([]);

  useEffect(() => {
    fetch('api/all-news/')
      .then(response => response.json())
      .then(data => setAllNews(data.allNews))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>All News</h1>
      <ul>
        {allNews.map(news => (            
          <li key={news.id}>
            <h2>{news.title}</h2>
            <p>{news.content}</p>
          </li>
        ))} 
      </ul>
    </div>
  );
}

export default AllNews;


