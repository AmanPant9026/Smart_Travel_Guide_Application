package com.baecon.practice.ExampleItem1;

import java.io.Serializable;

/**
 * Model class to get and set Place Data with Adapter
 */
public class Recreation implements Serializable {
    private final int restaurantImageId;
    private final String restaurantTitle;
    private final String restaurantRating;
    private final String restaurantType;
    private final String restaurantPhone;
    private final String restaurantTime;
    private final String restaurantLocation;
    private final String restaurantWebsite;

    public Recreation(int imageId, String title, String rating, String type, String phone, String time, String location, String website) {
        this.restaurantImageId = imageId;
        this.restaurantTitle = title;
        this.restaurantRating = rating;
        this.restaurantType = type;
        this.restaurantPhone = phone;
        this.restaurantTime = time;
        this.restaurantLocation = location;
        this.restaurantWebsite = website;
    }

    public int getRestaurantImageId() {
        return restaurantImageId;
    }

    public String getRestaurantTitle() {
        return restaurantTitle;
    }

    public String getRestaurantRating() {
        return restaurantRating;
    }

    public String getRestaurantType() {
        return restaurantType;
    }

    public String getRestaurantPhone() {
        return restaurantPhone;
    }

    public String getRestaurantTime() {
        return restaurantTime;
    }

    public String getRestaurantLocation() {
        return restaurantLocation;
    }

    public String getRestaurantWebsite() {
        return restaurantWebsite;
    }
}