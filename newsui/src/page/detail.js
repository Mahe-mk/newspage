import React, { useState, useEffect, useContext } from 'react';
import axios from 'axios';
import { context } from '../App';
import { useNavigate,} from 'react-router-dom';
import { Button, Card, Col, NavLink, Row } from "react-bootstrap";

function Detail() {
  const [detail, setdetail] = useState([]);
  const {selectedNewsIdValue}  = useContext(context)
  const [selectedNewsId, setSelectedNewsId] = selectedNewsIdValue;
  const navigate = useNavigate();

  useEffect(() => {
        axios.get(`http://localhost:8000/detail/${selectedNewsId}`)
 .then((res) => setdetail(res.data))
 .catch(error => console.log(error));
  }, []);
  console.log("selectedNewsId",selectedNewsId);
  return (
    <div>
        <main className="container mt-3 mb-5" id>
        <Row className="row my-3">   
            <Col className="col-md-8">
                <Card className="card mb-3">
                    <Card.Img src={`http://localhost:8000`+ detail.image} className="card-img-top" />
                <Card.Body>
                    <Card.Title>{detail?.title}</Card.Title>
                    <hr/>
                    <Card.Text className="card-text">{detail?.detail}</Card.Text>
                </Card.Body>
                </Card>		
                <Button variant="success" size="sm"  onClick={() => navigate(-1)} >Go back</Button>
        </Col>	
        </Row>
        </main>
    </div>
  )
}
export default Detail