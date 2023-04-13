import React from 'react'

function Home() {
  return (
    <>
    <div className="container mt-3 mb-5">
	<div className="row my-3">
		<div className="col-md-7">
			<div className="card mb-3">
			  <img src="media/{{first_news.image}}" className="card-img-top" />
			  <div className="card-body">
			    {/* <h5 className="card-title">{{first_news.title}}</h5> */}
			    <h5 className="card-title">first title</h5>
			    <hr/>
			    <p className="card-text"><a href="/detail/{{first_news.id}}" className="btn btn-sm btn-success">Full News</a></p>
			  </div>
			</div>
		</div>
		<div className="col-md-5">
			{/* {% for news in three_news %} */}
			<div className="card">
			  <div className="row no-gutters">
			    <div className="col-md-4">
					<img src="media/{{news.image}}" className="card-img-top" />
			    </div>
			    <div className="col-md-8">
			      <div className="card-body">
			        <h5 className="card-title">news.title</h5>
			        <p className="card-text"><a href="/detail/{{news.id}}" className="btn btn-sm btn-success">Full News</a></p>
			      </div>
			    </div>
			  </div>
			</div>
			<hr/>
			{/* {% endfor %} */}
		</div>
	</div>
	{/* {% for category in three_categories %} */}
	<h3 className="border-bottom pb-1">category.title </h3>
	<div className="row my-4">
		{/* {% for news in category.news_set.all %} */}
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
		{/* {% endfor %} */}
	</div>
	{/* {% endfor %} */}
</div>
</>
  )
}

export default Home

