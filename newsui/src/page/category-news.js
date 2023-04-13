import React from 'react'

function CategoryNews() {
  return (
    <div>
        {/* {% extends 'main.html' %}
        {% block content %} */}
    <main className="container mt-3 mb-5">
        <h3 className="border-bottom pb-1 my-4">List of categories.title News</h3>	

        {/* {% for news in all_news %} */}
        <div className="card mb-4 shadow">
          <div className="row no-gutters">
            <div className="col-md-3">
                <img 	src="/media/{{news.image}}" className="card-img-top" />
            </div>
            <div className="col-md-8">
              <div className="card-body">
                <h5 className="card-title">news.title</h5>
                <p className="card-text">news.detail</p>
                <p className="card-text"><a href="/detail/{{news.id}}" className="btn btn-sm btn-success">Read Full</a></p>			
              </div>
            </div>
          </div>
        </div>	
        {/* {% endfor %} */}
        <p  className="card-text"><a href="/all-category" className="btn btn-sm btn-success">Previous Page</a></p> 
    </main>
    {/* {% endblock %} */}
    </div>
  )
}

export default CategoryNews