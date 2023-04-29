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
import FavCategories from './page/Fav_Categories';
import { createContext, useEffect, useState } from 'react';
import { data } from './app-data';
import SignInView from './page/signin';

export const context=createContext();


function App() {
const [selectedNewsId, setSelectedNewsId] = useState(data().selectedNewsId);
const [selectedCategoryId, setSelectedCategoryId] = useState(data().selectedCategoryId);

  return (
    <div className="App">
      <context.Provider value={{
        selectedNewsIdValue:[selectedNewsId, setSelectedNewsId],
        selectedCategoryIdValue:[selectedCategoryId, setSelectedCategoryId]
      }}>
      <AppHeader/>
      {/* <Home/>
      <AllNews/> */}

      <BrowserRouter>
      <Routes>
          <Route path="/" element={<Home />} />
          <Route path="all-news" element={<AllNews />} />
          <Route path="category" element={<Category />} />
          <Route path="weather" element={<Weather />} />
          <Route path='categorynews' element={<CategoryNews/>} />
          <Route path="myCategory" element={<FavCategories/>} />
          <Route path="detail" element={<Detail/>} />
          <Route path="signin" element={<SignInView/>} />
      </Routes>
    </BrowserRouter>
    </context.Provider>
    </div>
  );
}
export default App;