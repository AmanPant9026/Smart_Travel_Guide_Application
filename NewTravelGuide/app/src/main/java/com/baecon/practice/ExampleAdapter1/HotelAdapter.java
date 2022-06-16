package com.baecon.practice.ExampleAdapter1;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.RatingBar;
import android.widget.TextView;

import androidx.recyclerview.widget.RecyclerView;

import com.baecon.practice.ExampleItem1.Hotel;
import com.baecon.practice.R;

import java.util.ArrayList;
import java.util.List;


public class HotelAdapter extends RecyclerView.Adapter<HotelAdapter.ExampleViewHolder> {
    private List<Hotel> exampleList;
    private List<Hotel> exampleListFull;
    private Context mContext;

    class ExampleViewHolder extends RecyclerView.ViewHolder {
        ImageView hotelImage;
        TextView hotelTitle;
        TextView hotelRating;
        RatingBar hotelRatingBar;
        TextView hotelType;
        LinearLayout constraintLayout;

        ExampleViewHolder(View itemView) {
            super(itemView);

            this.hotelImage = (ImageView) itemView.findViewById(R.id.hotel_image);
            this.hotelTitle = (TextView) itemView.findViewById(R.id.hotel_name);
            this.hotelRating = (TextView) itemView.findViewById(R.id.rating);
            this.hotelRatingBar = (RatingBar) itemView.findViewById(R.id.ratingBar);
            this.hotelType = (TextView) itemView.findViewById(R.id.hotel_type);
            this.constraintLayout = (LinearLayout) itemView.findViewById(R.id.parent);

        }
    }

    public HotelAdapter(List<Hotel> exampleList2, Context context) {
       // this.mContext = context;
        this.exampleList = exampleList2;
        this.exampleListFull = new ArrayList(exampleList2);
    }

    public ExampleViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
       // mContext = parent.getContext();
        return new ExampleViewHolder(LayoutInflater.from(parent.getContext()).inflate(R.layout.layout_hotel_fragment, parent, false));
    }
    @Override
    public void onAttachedToRecyclerView(RecyclerView recyclerView) {
        super.onAttachedToRecyclerView(recyclerView);
        this.mContext = recyclerView.getContext();
    }
    
    public void onBindViewHolder(ExampleViewHolder holder, int position) {

        final Hotel currentItem = (Hotel) this.exampleList.get(position);

        holder.hotelImage.setImageResource(currentItem.getHotelImageId());
        holder.hotelTitle.setText(currentItem.getHotelTitle());
        holder.hotelRating.setText(currentItem.getHotelRating());
        holder.hotelRatingBar.setRating(Float.parseFloat(currentItem.getHotelRating()));
        holder.hotelType.setText(currentItem.getHotelType());
//        holder.parentLayout.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//                Intent intent = new Intent(mContext, ViewStatus.class);
//                intent.putExtra("data", currentItem.getmText3());
//                intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
//                mContext.startActivity(intent);
//            }
//        });
    }

    public int getItemCount() {
        return this.exampleList.size();
    }

    /* access modifiers changed from: 0000 */
    public void setFilter(List<Hotel> filterdNames) {
        this.exampleList = filterdNames;
        notifyDataSetChanged();
    }
}