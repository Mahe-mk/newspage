import React, { useState, useEffect, useContext } from 'react';
import axios from 'axios';
import { context } from '../App';
import { setData } from "../app-data";
import { Button, Card, Col, NavLink, Row } from "react-bootstrap";
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
          <Card className="card mb-4 shadow" key={newsItem.id}>
            <Row className="row no-gutters">
              <Col className="col-md-3">
                <Card.Img src={`http://localhost:8000${newsItem.image}`} className="card-img-top" />
              </Col>
              <Col className="col-md-8">
                <Card.Body>
                  <Card.Title className="card-title">{newsItem.title}</Card.Title>
                  <Card.Text className="card-text">{newsItem.detail}</Card.Text>
                  <Button variant="success" size="sm"  href="/detail"  onClick={()=>handleClick(newsItem.id)}>Read Full</Button>
                </Card.Body>
              </Col>
            </Row>
          </Card>
        ))}
        <Button variant="success" size="sm"  onClick={() => navigate(-1)} >Go back</Button>
      </main>
    </div>
  )
}
export default CategoryNews;