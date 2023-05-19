import React from 'react'
import { Button, Col, Row } from 'react-bootstrap';

function AppHeader() {
	return (<>
		<nav className="navbar navbar-exapand-lg navbar-dark bg-dark">
			<div className="container row d-flex p-2 justify-content-around" >
				<a className="navbar-brand text-decoration-none">M_K News</a>
				<a className="text-decoration-none" href="http://localhost:8000/admin/">Admin</a>
				<a className="text-decoration-none" href="/">Home</a>
				<a className="text-decoration-none" href="/all-news">All News</a>
				<a className="text-decoration-none" href="/Category">All Categories</a>
				<a className="text-decoration-none" href="/Weather">Weather </a>
				</div>
				<div className ="d-flex p-2 justify-content-end">
				<Row><Col  className="col-lg-0" ><a className="text-decoration-none" href="/myCategory">My Favourites </a>
				</Col>
				<Col lg={6}><div className="fs-1 text-end font-monospace fw-bold text-white">Welcome </div></Col>
				<Col lg={6}><a className="text-decoration-none" href="/signout">SingOut </a> </Col>
				<Col lg={12}><a className="text-decoration-none" href="/signin">SignIn </a></Col>
				</Row>
			</div>
		</nav>
	</>
	)
}
export default AppHeader