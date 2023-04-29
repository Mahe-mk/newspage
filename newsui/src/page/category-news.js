import React, { useState, useEffect, useContext } from 'react';
import axios from 'axios';
import { context } from '../App';
import { setData } from "../app-data";
import { Button, NavLink } from "react-bootstrap";
import { useNavigate,} from 'react-router-dom';

function CategoryNews() {
  const [news, setNews] = useState([]);
  const {selectedCategoryIdValue}  = useContext(context)
  const [selectedCategoryId, setSelectedCategoryId] = selectedCategoryIdValue;
  const navigate = useNavigate();

  useEffect(() => {
    async function fetchNews() {
      const response = await axios.get(`http://127.0.0.1:8000/category/${selectedCategoryId}`);
      setNews(response.data.all_news);
    }
    fetchNews();
  }, []);

  const handleClick =(id)=>{
    setData("selectedNewsId",id)
  }
  return (
    <div>
      <main className="container mt-3 mb-5">
        <h3 className="border-bottom pb-1 my-4">List of News</h3>
        {news.map((newsItem) => (
          <div className="card mb-4 shadow" key={newsItem.id}>
            <div className="row no-gutters">
              <div className="col-md-3">
                <img src={`http://localhost:8000${newsItem.image}`} className="card-img-top" />
              </div>
              <div className="col-md-8">
                <div className="card-body">
                  <h5 className="card-title">{newsItem.title}</h5>
                  <p className="card-text">{newsItem.detail}</p>
                  <p className="card-text">
                  <Button className="btn btn-sm btn-success" href="/detail"  onClick={()=>handleClick(newsItem.id)}>Read Full</Button>

                    {/* <a href={`/detail`} className="btn btn-sm btn-success">Read Full</a>			 */}</p>
                </div>
              </div>
            </div>
          </div>
        ))}
        {/* <p className="card-text"><a href="/category" className="btn btn-sm btn-success">Previous Page</a></p>  */}
        <p className="card-text"><button onClick={() => navigate(-1)}className="btn btn-sm btn-success">Go back</button></p>
      </main>
    </div>
  )
}
export default CategoryNews;