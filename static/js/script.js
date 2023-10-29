document.addEventListener("DOMContentLoaded", function () {
    const productContainer = document.getElementById("product-container");

    const products = [
        {
            name: "Running Shoes",
            description: "High-performance running shoes for all terrains.",
            price: getRandomPrice(),
            image: "images/shoe1.jpg",
        },
        {
            name: "Casual Sneakers",
            description: "Stylish and comfortable sneakers for everyday wear.",
            price: getRandomPrice(),
            image: "images/shoe2.jpg",
        },
        // Add more product details here
    ];

    products.forEach((product, index) => {
        const productTile = productContainer.children[index];
        const productName = productTile.querySelector("h2");
        const productDescription = productTile.querySelector(".description");
        const productPrice = productTile.querySelector(".price");
        const productImage = productTile.querySelector("img");

        // Update product details with random data
        productName.textContent = product.name;
        productDescription.textContent = product.description;
        productPrice.textContent = `$${product.price}`;
        productImage.src = product.image;
    });
});

function getRandomPrice() {
    return (Math.random() * (100 - 20) + 20).toFixed(2);
}
