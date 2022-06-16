package com.baecon.practice.ExampleAdapter1;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.RatingBar;
import android.widget.TextView;

import com.baecon.practice.ExampleItem1.Place;
import com.baecon.practice.R;

import java.util.ArrayList;
import java.util.List;

import androidx.cardview.widget.CardView;
import androidx.recyclerview.widget.RecyclerView;


public class PlaceAdapter extends RecyclerView.Adapter<PlaceAdapter.ExampleViewHolder> {
    private List<Place> exampleList;
    private List<Place> exampleListFull;
    private Context mContext;

    class ExampleViewHolder extends RecyclerView.ViewHolder {
        TextView placeTitle;
        ImageView placeImg;
        TextView placeRating;
        RatingBar placeRatingBar;
        TextView placeType;
        CardView cardView;

        ExampleViewHolder(View itemView) {
            super(itemView);

            this.placeTitle = (TextView) itemView.findViewById(R.id.place_name);
            this.placeImg = (ImageView) itemView.findViewById(R.id.place_image);
            this.placeRating = (TextView) itemView.findViewById(R.id.rating);
            this.placeRatingBar = (RatingBar) itemView.findViewById(R.id.ratingBar);
            this.placeType = (TextView) itemView.findViewById(R.id.place_type);
            this.cardView = (CardView) itemView.findViewById(R.id.cardView);

        }
    }

    public PlaceAdapter(List<Place> exampleList2, Context context) {
       // this.mContext = context;
        this.exampleList = exampleList2;
        this.exampleListFull = new ArrayList(exampleList2);
    }

    public ExampleViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
       // mContext = parent.getContext();
        return new ExampleViewHolder(LayoutInflater.from(parent.getContext()).inflate(R.layout.layout_place_fragment, parent, false));
    }
    @Override
    public void onAttachedToRecyclerView(RecyclerView recyclerView) {
        super.onAttachedToRecyclerView(recyclerView);
        this.mContext = recyclerView.getContext();
    }
    
    public void onBindViewHolder(ExampleViewHolder holder, int position) {

        final Place currentItem = (Place) this.exampleList.get(position);

        holder.placeTitle.setText(currentItem.getPlaceTitle());
        holder.placeImg.setImageResource(currentItem.getPlaceImageId());
        holder.placeRating.setText(currentItem.getPlaceRating());
        holder.placeRatingBar.setRating(Float.parseFloat(currentItem.getPlaceRating()));
        holder.placeType.setText(currentItem.getPlaceType());
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
    public void setFilter(List<Place> filterdNames) {
        this.exampleList = filterdNames;
        notifyDataSetChanged();
    }
}