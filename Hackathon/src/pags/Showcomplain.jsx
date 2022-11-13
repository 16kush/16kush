import { collection, getDocs, query } from "firebase/firestore";
import React,{  useEffect, useState } from "react";
import { db } from "../firebase";


const Showcomplaint = () => {
  const [details, setDetails] = useState([]);
  const userData = async () => {
    const q = query(collection(db, "complain"));

    const querySnapshot = await getDocs(q);
    const data = querySnapshot.docs.map((doc) => ({
      // doc.data() is never undefined for query doc snapshots
      ...doc.data(),
      id: doc.id,
    }));
    setDetails(data);
  };
  useEffect(() => {
    userData();
  }, []);
  

  return (
    <div className="formContainer_rep">
      {details.map((val, id) => {
        return <div className="formWrapper_rep">
                <p key={id} className="pt-2 ">Name : {val.name}</p>
                <p key={id} className="pt-2 ">Label : {val.label}</p>
                <p key={id} className="pt-2 ">Describe : {val.discribe}</p>
              </div>
          })}
    </div>
  );
};

export default Showcomplaint;