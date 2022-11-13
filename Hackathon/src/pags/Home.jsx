import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { useUserAuth ,user} from "../context/AuthContext";
import Gov from "./gov";
// import { getDownloadURL, ref, uploadBytes } from "firebase/storage";
// import { db, storage } from "../firebase";
// import { doc, setDoc } from "firebase/firestore";
// import './App.css';
// import * as ReactBootStrap from "react-bootstrap";
import './home.css';




const Home = () => {
  const { logOut ,user} = useUserAuth();
  const navigate = useNavigate();
  const handleLogout = async () => {
    try {
      await logOut();
      navigate("/");
    } catch (error) {
      console.log(error.message);
    }
  };

  return (
<>
<div className="NAV">
    <ul className="nav nav-pills">
  <li className="nav-item">
    <button onClick={handleLogout}>sing out</button>
  </li>
</ul>
    </div>
    <div>

    </div >
    <div className="mm">
    <div className="image">
     <img src="https://wallpaperaccess.com/full/1386158.png" alt="" />
    </div>
    <div>
    <div className="main">
     <Link to='/addcomplain'><button type="button" class="btn btn-primary">Add Complaint</button></Link>
     </div>
    <div className="main">
    <Link to ='/showcomplaint'><button type="button" class="btn btn-primary">Show Complaint</button></Link>
    </div>
    </div>
    
    </div>
    


</>
  
 
   
    
  );
};

export default Home;