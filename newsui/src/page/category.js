import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Button, Card, Col, Row} from "react-bootstrap";
import { setData } from "../app-data";


function CategoryList() {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    async function fetchCategories() {
      const response = await axios.get('http://localhost:8000/all-category');
      setCategories(response.data);
    }
    fetchCategories();
  }, []);

  const handleClick =(id)=>{
    setData("selectedCategoryId",id)
  }
  return (
    <div>
      <h3>All Categories:</h3>
      {categories.map((category) => (
        <div>
          <Row className='d-flex justify-content-center'>
          <Col md={4} sm={4} >
          <Card key={category.id}>
          <Card.Title>{category.title}</Card.Title>
          <Card.Img src={'http://localhost:8000' + category.category_image} alt={category.title} className="card-img-top" />
          <div className='pt-3'>
            <Button className="btn btn-sm btn-success" href="/categorynews"  onClick={()=>handleClick(category.id)}>Full News</Button>
          </div>
          </Card>
          </Col>
          </Row>
        </div>
      ))}
    </div>
  );
}
export default CategoryList;