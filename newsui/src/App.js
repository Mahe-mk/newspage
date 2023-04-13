import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import AppHeader from './component/app-header';
import Home from './page/home';
import AllNews from './page/all-news';
import Category from './page/category';
import CategoryNews from './page/category-news';
import Weather from './page/weather';
import Detail from './page/detail';
import Fav_Categories from './page/Fav_Categories';

function App() {
  return (
    <div className="App">
      <AppHeader/>
      {/* <Home/>
      <AllNews/> */}
      <BrowserRouter>
      <Routes>
          <Route path="/" element={<Home />} />
          <Route path="all-news" element={<AllNews />} />
          <Route path="Category" element={<Category />} />
          <Route path="weather" element={<Weather />} />
          <Route path='CategoryNews' element={<CategoryNews/>} />
          <Route path="Fav_Category" element={<Fav_Categories />} />
      </Routes>
    </BrowserRouter>
    </div>
  );
}
export default App;