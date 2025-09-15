package com.example.retail;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

@SpringBootApplication
@RestController
public class RetailApplication {

    @GetMapping("/")
    public String health() {
        return "Retail Java App is running";
    }

    @PostMapping("/order")
    public String createOrder(@RequestBody Order order) {
        // simulate order and maybe call Python API
        return "Order accepted for product: " + order.getProduct();
    }

    @GetMapping("/forecast")
    public String getForecast() {
        RestTemplate restTemplate = new RestTemplate();
        String url = "http://forecast.cloud-ai.svc.cluster.local:8000/forecast";
        return restTemplate.postForObject(url,
                Map.of("series", List.of(1,2,3,4)),
                String.class);
    }

    public static void main(String[] args) {
        SpringApplication.run(RetailApplication.class, args);
    }
}

class Order {
    private String product;
    public String getProduct() { return product; }
    public void setProduct(String product) { this.product = product; }
}
