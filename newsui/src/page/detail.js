import React, { useState, useEffect, useContext } from 'react';
import axios from 'axios';
import { context } from '../App';
import { useNavigate,} from 'react-router-dom';
// import useAppContext from "../context";

function Detail() {
  const [detail, setdetail] = useState([]);
  const {selectedNewsIdValue}  = useContext(context)
  const [selectedNewsId, setSelectedNewsId] = selectedNewsIdValue;
  const navigate = useNavigate();

  useEffect(() => {
    // async function fetchdetail() {
    //   const response = await axios.get('http://localhost:8000/detail/'+selectedId);
    //   setdetail(response.data);
    // }
    // fetchdetail();
  
    axios.get(`http://localhost:8000/detail/${selectedNewsId}`)
 .then((res) => setdetail(res.data))
 .catch(error => console.log(error));

  }, []);
  console.log("selectedNewsId",selectedNewsId);
  // console.log("selectedId", typeof selectedId);
  return (
    <div>
      {/* {detail?.map(news => ( */}
        <main className="container mt-3 mb-5" id>
        <div className="row my-3">   
            <div className="col-md-8">
                <div className="card mb-3">
                    <img src={`http://localhost:8000`+ detail.image} className="card-img-top" />
                <div className="card-body">
                    <p className="card-title h1">{detail?.title}</p>
                    <hr/>
                    <p className="card-text">{detail?.detail}</p>
                </div>
                </div>		
                <p className="card-text"><button onClick={() => navigate(-1)}className="btn btn-sm btn-success">Go back</button></p>
                {/* <p className="card-text"><a href="/all-news" className="btn btn-sm btn-success">Previous Page</a></p> */}
        </div>	
        </div>
        </main>
      {/* ))} */}
    </div>
  )
}
export default Detail

// import React, { useState, useEffect } from 'react';
// import axios from 'axios';

// function Detail() {
//   const [detail, setDetail] = useState({});

//   useEffect(() => {
//     async function fetchDetail() {
//       const response = await axios.get('http://localhost:8000/detail/1');
//       setDetail(response.data);
//     }
//     fetchDetail();
//   }, []);

//   return (
//     <div>
//       <main className="container mt-3 mb-5">
//         <div className="row my-3">   
//             <div className="col-md-8">
//                 <div className="card mb-3">
//                     <img src={`http://localhost:8000${detail.image}`} className="card-img-top" />
//                     <div className="card-body">
//                         <p className="card-title h1">{detail.title}</p>
//                         <hr/>
//                         <p className="card-text">{detail.detail}</p>
//                     </div>
//                 </div>		
//                 <p className="card-text"><a href="/all-news" className="btn btn-sm btn-success">Previous Page</a></p>
//             </div>	
//         </div>
//       </main>
//     </div>
//   )
// }
// export default Detail
