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
				<div className="row my-3">
					<div className="col-md-7">
						<div className="card mb-3">
							<img src={'http://localhost:8000' + mainData.first_news?.image} alt={mainData.first_news?.image} className="card-img-top" />
							<div className="card-body">
								<h5 className="card-title">{mainData.first_news?.title}</h5>
								{/* <h5 className="card-title">first title</h5> */}
								<hr />
								{/* <p className="card-text"><a href="/detail/" className="btn btn-sm btn-success">Full News</a></p> */}
								<Button className="btn btn-sm btn-success" href="/detail"  onClick={()=>handleClick(mainData.first_news.id)}>Full News</Button>
							</div>
						</div>
					</div>

					<div className="col-md-5">
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
											Full News
        </Button></Card.Text>
										</Card.Body>
									</Col>
								</Row>
							</Card>
						))}
						<hr />
					</div>
				</div>
				{/* 
	<div>
	<h3 className="border-bottom pb-1">category.title </h3>
	<div className="row my-4">
		{% for news in category.news_set.all %}
			<div className="col-md-3">
				<div className="card mb-3 shadow">
				<img src="media/{{news.image}}" className="card-img-top" />
				<div className="card-body">
					<h5 className="card-title">news.title</h5>
					<hr/>
					<p className="card-text"><a href="/detail/{{news.id}}" className="btn btn-sm btn-success">Full News</a></p>
				</div>
				</div>
			</div>
		{% endfor %}
	</div>
	</div>
	{% endfor %} */}

				{mainData?.three_categories?.map((category) => (
					<div key={category.id}>
						<h3 className="border-bottom pb-1">{category.title}</h3>
						<div className="row my-4">
							{category?.news?.map((news) => (
								<div className="col-md-3" key={news.id}>
									<div className="card mb-3 shadow">
										<img src={`http://localhost:8000` + news?.image} className="card-img-top" width={280} height={280} alt={category.title} />

										<div className="card-body">

											<h5 className="card-title">{news.title}</h5>
											<hr />
											{/* <p className="card-text"><a href={`/detail`} className="btn btn-sm btn-success">Full News</a></p> */}
											<Button variant="success" size="sm" href="/detail" onClick={()=>handleClick(news.id)}>Full News</Button>
										</div>
									</div>
								</div>
							))}
						</div>
					</div>
				))}	
			</div>
		</>
	)
}
export default Home