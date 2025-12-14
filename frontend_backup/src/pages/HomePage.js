import React, { useEffect, useState } from "react";
import { getSweets, purchaseSweet } from "../services/api";

function HomePage() {
  const [sweets, setSweets] = useState([]);

  useEffect(() => {
    fetchSweets();
  }, []);

  const fetchSweets = async () => {
    const response = await getSweets();
    setSweets(response.data);
  };

  const handlePurchase = async (id) => {
    await purchaseSweet(id);
    fetchSweets();
  };

  return (
    <div>
      <h1>Sweet Shop</h1>
      <ul>
        {sweets.map((sweet) => (
          <li key={sweet.id}>
            {sweet.name} - ${sweet.price} - Qty: {sweet.quantity}
            <button disabled={sweet.quantity === 0} onClick={() => handlePurchase(sweet.id)}>
              Purchase
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default HomePage;
