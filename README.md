# Pizza ordering service
Pizza ordering restful api using django rest framework

### Prerequisites

Install docker: [Docs](https://docs.docker.com/install/)

### Installing & Running

```
git clone https://github.com/titans55/pizza-ordering-service.git
docker-compose up
```
After that you would be able to send requests to endpoints of api.
Go to [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/) for to see the default basic root view of drf



## Common API use cases

  1. Order pizzas
     - Specify the desired flavors of pizza, the number of pizzas and their size.
     - An order contains the information regarding the customer.
     - Track the status of delivery.
     - Order the same flavor of pizza but with different sizes multiple times
  2. Update an order
     - Update the details — flavours, count, sizes — of an order
     - Disable update of an order for some statutes of delivery (e.g. delivered).
     - Change the status of delivery.
  3. Remove an order
  4. Retrieve an order
     - Retrieve the order by its identifier(url).
  5. List orders
		 - Retrieve all the orders at once.
     - Allow filtering by status / customer.

#### Note

  Authentication is not implemented in that project. When it does, customer_id in the Order model could be changed as a foreign Key which links to Customer(User) model
