
export const data = ()=> {
    return {
        selectedNewsId : getData("selectedNewsId"),
        selectedCategoryId:getData("selectedCategoryId")
    }
}

const getData = (key)=>{
    return localStorage.getItem(key);
}

export const setData = (key, value) => {
    if (value) {
     localStorage.setItem(key, value);  
   } else {
    localStorage.setItem(key, null);
    }
    };

const getJSONValue = key => {
    const jsonText = getData(key);
    return jsonText?.includes("{") ? JSON.parse(jsonText) : {};
};

const setJSONValue = (key, value) => {
    if (value instanceof Object) {
        setData(key, JSON.stringify(value));
    }
};