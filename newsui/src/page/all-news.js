import React, { useContext, useEffect, useState } from "react";
import axios from "axios";
import { Button, Card,Col, NavLink, Row } from "react-bootstrap";
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
        <Card key={news.id} className="card mb-4 shadow">
          <Row className="row no-gutters">
            <Col className="col-md-3">
              <Card.Img src={`http://localhost:8000`+news.image} className="card-img-top" />
            </Col>
            <Col className="col-md-8">
              <Card.Body className="card-body">
                <Card.Title className="card-title">{news.title}</Card.Title>
                <Card.Text className="card-text">{news.detail}</Card.Text>
                <Button className="btn btn-sm btn-success" href="/detail"  onClick={()=>handleClick(news.id)}>Full News</Button>
              </Card.Body>
            </Col>
          </Row>
        </Card>
      ))}
    </div>
  );
}
export default AllNews;
