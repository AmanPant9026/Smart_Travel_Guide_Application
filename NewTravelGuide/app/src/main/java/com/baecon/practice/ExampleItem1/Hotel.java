package com.baecon.practice.ExampleItem1;

import java.io.Serializable;

/**
 * Model class to get and set Place Data with Adapter
 */
public class Hotel implements Serializable {
    private final int hotelImageId;
    private final String hotelTitle;
    private final String hotelRating;
    private final String hotelPhone;
    private final String hotelType;
    private final String hotelLocation;

    public Hotel(int imageId, String title, String rating, String phone, String type, String location) {
        this.hotelImageId = imageId;
        this.hotelTitle = title;
        this.hotelRating = rating;
        this.hotelPhone = phone;
        this.hotelType = type;
        this.hotelLocation = location;
    }

    public int getHotelImageId() {
        return hotelImageId;
    }

    public String getHotelTitle() {
        return hotelTitle;
    }

    public String getHotelRating() {
        return hotelRating;
    }

    public String getHotelPhone() {
        return hotelPhone;
    }

    public String getHotelType() {
        return hotelType;
    }

    public String getHotelLocation() {
        return hotelLocation;
    }
}