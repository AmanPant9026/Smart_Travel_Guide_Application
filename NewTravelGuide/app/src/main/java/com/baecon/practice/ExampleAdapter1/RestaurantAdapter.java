package com.baecon.practice.ExampleAdapter1;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.RatingBar;
import android.widget.TextView;

import androidx.cardview.widget.CardView;
import androidx.recyclerview.widget.RecyclerView;

import com.baecon.practice.ExampleItem1.Restaurant;
import com.baecon.practice.R;

import java.util.ArrayList;
import java.util.List;


public class RestaurantAdapter extends RecyclerView.Adapter<RestaurantAdapter.ExampleViewHolder> {
    private List<Restaurant> exampleList;
    private List<Restaurant> exampleListFull;
    private Context mContext;

    class ExampleViewHolder extends RecyclerView.ViewHolder {

        ImageView restoImg;
        TextView restoTitle;
        TextView restoType;
        TextView restoRating;
        RatingBar restoRatingBar;
        CardView cardView;

        ExampleViewHolder(View itemView) {
            super(itemView);

            this.restoImg = (ImageView) itemView.findViewById(R.id.restaurant_image);
            this.restoTitle = (TextView) itemView.findViewById(R.id.restaurant_name);
            this.restoType = (TextView) itemView.findViewById(R.id.restaurant_type);
            this.restoRating = (TextView) itemView.findViewById(R.id.rating);
            this.restoRatingBar = (RatingBar) itemView.findViewById(R.id.ratingBar);
            this.cardView = (CardView) itemView.findViewById(R.id.cardView);
        }
    }

    public RestaurantAdapter(List<Restaurant> exampleList2, Context context) {
       // this.mContext = context;
        this.exampleList = exampleList2;
        this.exampleListFull = new ArrayList(exampleList2);
    }

    public ExampleViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
       // mContext = parent.getContext();
        return new ExampleViewHolder(LayoutInflater.from(parent.getContext()).inflate(R.layout.layout_restaurant_fragment, parent, false));
    }
    @Override
    public void onAttachedToRecyclerView(RecyclerView recyclerView) {
        super.onAttachedToRecyclerView(recyclerView);
        this.mContext = recyclerView.getContext();
    }
    
    public void onBindViewHolder(ExampleViewHolder holder, int position) {

        final Restaurant currentItem = (Restaurant) this.exampleList.get(position);

        holder.restoImg.setImageResource(currentItem.getRestaurantImageId());
        holder.restoTitle.setText(currentItem.getRestaurantTitle());
        holder.restoType.setText(currentItem.getRestaurantType());
        holder.restoRating.setText(currentItem.getRestaurantRating());
        holder.restoRatingBar.setRating(Float.parseFloat(currentItem.getRestaurantRating()));
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
    public void setFilter(List<Restaurant> filterdNames) {
        this.exampleList = filterdNames;
        notifyDataSetChanged();
    }
}