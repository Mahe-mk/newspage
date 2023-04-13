import React from 'react'

function Category() {
  return (
    <div>
            {/* {% extends 'main.html' %} */}
{/* {% block content %} */}
<main className="container mt-3 mb-5">
	<h3 className="border-bottom pb-1 my-4">All Categories</h3>
	<div className="row">
		{/* <!-- Category Box --> */}
		{/* {% for cat in cats %} */}
		<div className="col-md-4">
			<div className="card mb-3 shadow">
            <img src="/media/{{cat.category_image}}" className="card-img-top" />
			  <div className="card-body">
			    <h5 className="card-title">cat.title</h5>
			    <hr/>
			    <p className="card-text"><a href="category/{{cat.id}}" className="btn btn-sm btn-success">All News</a></p>
			  </div>
			</div>
		</div>
		{/* {% endfor %} */}
	</div>
</main>
{/* {% endblock %} */}

    </div>
  )
}

export default Category














// import React, { useEffect, useState } from 'react';

// function Category() {
//   const [categories, setCategories] = useState([]);

//   useEffect(() => {
//     fetch('/api/categories/')
//       .then(response => response.json())
//       .then(data => setCategories(data.categories))
//       .catch(error => console.log(error));
//   }, []);

//   return (
//     <div>
//       <h1>All Categories</h1>
//       <ul>
//         {categories.map(category => (
//           <li key={category.id}>{category.title}</li>
//         ))}
//       </ul>
//     </div>
//   );
// }

// export default Category;
