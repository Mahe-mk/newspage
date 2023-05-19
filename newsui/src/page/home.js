import React, { useState, useEffect } from 'react';
import axios from 'axios';
// import Card from 'react-bootstrap/Card';
import { Col, Row, Button ,Card } from 'react-bootstrap';
import { setData } from '../app-data';

function Home() {
	const [mainData, setMainData] = useState([]);
	useEffect(() => {
		axios.get(`http://localhost:8000`)
			.then((res) => setMainData(res.data))
			.catch(error => console.log(error));
	}, []);
	console.log(mainData)
	const handleClick =(id)=>{
		setData("selectedNewsId",id)
	  }
	return (
		<>
			<div className="container mt-3 mb-5">
				<Row className="row my-3">
					<Col className="col-md-7">
						<Card>
							<Card.Img src={'http://localhost:8000' + mainData.first_news?.image} alt={mainData.first_news?.image} className="card-img-top" />
							<Card.Body>
								<Card.Title>{mainData.first_news?.title}</Card.Title>
								<hr />
									<Button variant="success" size="sm" href="/detail"  onClick={()=>handleClick(mainData.first_news.id)}>Full News</Button>
							</Card.Body>
						</Card>
					</Col>

					<Col className="col-md-5">
						{mainData?.three_news?.map((news) => (
							<Card className="card">
								<Row className="row no-gutters">
									<Col className="col-md-4">
										<Card.Img  variant="top" src={`http://localhost:8000` + news.image}  />
									</Col>
									<Col className="col-md-8">
										<Card.Body>
											<Card.Title className="card-title">{news?.title}</Card.Title>
											<Card.Text className="card-text">
											<Button variant="success" size="sm" href="/detail" onClick={()=>handleClick(news.id)}>
											Full News</Button>
        									</Card.Text>
										</Card.Body>
									</Col>
								</Row>
							</Card>
						))}
						<hr />
					</Col>
				</Row>
				
				{mainData?.three_categories?.map((category) => (
					<div key={category.id}>
						<h3 className="border-bottom pb-1">{category.title}</h3>
						<Row className="row my-2">
							{category?.news?.map((news) => (
								<Col className="col-md-3" key={news.id}>
									<Card className="card mb-3 shadow">
										<Card.Img src={`http://localhost:8000` + news?.image} className="card-img-top" width={280} height={280} alt={category.title} />
										<Card.Body>
											<Card.Title className="card-title">{news.title}</Card.Title>
											<hr />
											<Button variant="success" size="sm" href="/detail" onClick={()=>handleClick(news.id)}>Full News</Button>
										</Card.Body>
									</Card>
								</Col>
							))}
						</Row>
					</div>
				))}	
			</div>
		</>
	)
}
export default Home