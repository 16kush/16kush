import { collection, getDocs, query, where } from "firebase/firestore";
import React,{  useEffect, useState } from "react";
import { db } from "../firebase";


const Gov = () => {
  const [chack_label,Setlable] = useState("");
  const [details, setDetails] = useState([]);
  const userData = async (e) => {
    e.preventDefault();
    const q = query(collection(db, "complain"),where("label", "==", chack_label));

    const querySnapshot = await getDocs(q);
    const data = querySnapshot.docs.map((doc) => ({
      ...doc.data(),
      id: doc.id,
    }));
    setDetails(data);
  };

  return (
    <div className="formContainer_rep">
      {details.map((val, id) => {
        return <div className="formWrapper_rep">
                <p key={id} className="pt-2 ">Name : {val.name}</p>
                <p key={id} className="pt-2 ">Label : {val.label}</p>
                <p key={id} className="pt-2 ">Describe : {val.discribe}</p>
              </div>
          })}
          <form onSubmit={userData}>
           <input type="text" placeholder="Search Label" onChange={(e) => Setlable(e.target.value)}/>
          <button>Search</button>
          </form>
    </div>
  );
};

export default Gov;