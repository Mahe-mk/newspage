import React, { useContext, useEffect, useState } from "react";
import axios from "axios";
import { Button, NavLink } from "react-bootstrap";
import { context } from "../App";
import { setData } from "../app-data";

function AllNews() {
  const [newsList, setNewsList] = useState([]);
  useEffect(() => {
    axios.get("http://localhost:8000/all-news")
 .then((res) => setNewsList(res.data))
 .catch(error => console.log(error));
    // fetchNewsData();
  }, []);

  const handleClick =(id)=>{
    setData("selectedNewsId",id)

  }

  return (
    <div className="container mt-3 mb-5">
      <h3 className="border-bottom pb-1 my-4">All News</h3>
      {newsList?.map(news => (
        <div key={news.id} className="card mb-4 shadow">
          <div className="row no-gutters">
            <div className="col-md-3">
              <img src={`http://localhost:8000`+news.image} className="card-img-top" />
            </div>
            <div className="col-md-8">
              <div className="card-body">
                <h5 className="card-title">{news.title}</h5>
                <p className="card-text">{news.detail}</p>
                <Button className="btn btn-sm btn-success" href="/detail"  onClick={()=>handleClick(news.id)}>Full News</Button>
              </div>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}
export default AllNews;


