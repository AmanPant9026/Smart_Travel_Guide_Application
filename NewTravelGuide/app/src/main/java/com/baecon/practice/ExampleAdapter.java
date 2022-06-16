package com.baecon.practice;

import android.content.Context;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.List;

import androidx.recyclerview.widget.RecyclerView;


public class ExampleAdapter extends RecyclerView.Adapter<ExampleAdapter.ExampleViewHolder> {
    private List<ExampleItem> exampleList;
    private List<ExampleItem> exampleListFull;
    private Context mContext;

    class ExampleViewHolder extends RecyclerView.ViewHolder {
        ImageView imageView;
        TextView textView1;
        TextView textView2;
        TextView textView3;
        RelativeLayout parentLayout;

        ExampleViewHolder(View itemView) {
            super(itemView);

            this.imageView = (ImageView) itemView.findViewById(R.id.image_app);
            this.textView1 = (TextView) itemView.findViewById(R.id.textview1);
            this.textView2 = (TextView) itemView.findViewById(R.id.textview2);
            this.textView3 = (TextView) itemView.findViewById(R.id.textview3);
            this.parentLayout = (RelativeLayout) itemView.findViewById(R.id.container);

        }
    }

    public ExampleAdapter(List<ExampleItem> exampleList2, Context context) {
       // this.mContext = context;
        this.exampleList = exampleList2;
        this.exampleListFull = new ArrayList(exampleList2);
    }

    public ExampleViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
       // mContext = parent.getContext();
        return new ExampleViewHolder(LayoutInflater.from(parent.getContext()).inflate(R.layout.item_my_apps2, parent, false));
    }
    @Override
    public void onAttachedToRecyclerView(RecyclerView recyclerView) {
        super.onAttachedToRecyclerView(recyclerView);
        this.mContext = recyclerView.getContext();
    }
    
    public void onBindViewHolder(ExampleViewHolder holder, int position) {

        final ExampleItem currentItem = (ExampleItem) this.exampleList.get(position);
        holder.textView1.setText(currentItem.getmText1());
        holder.textView2.setText(currentItem.getmText2());
        holder.textView3.setText(currentItem.getmText3());
        holder.parentLayout.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(mContext, ViewStatus.class);
                intent.putExtra("data", currentItem.getmText3());
                intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                mContext.startActivity(intent);
            }
        });
    }

    public int getItemCount() {
        return this.exampleList.size();
    }

    /* access modifiers changed from: 0000 */
    public void setFilter(List<ExampleItem> filterdNames) {
        this.exampleList = filterdNames;
        notifyDataSetChanged();
    }
}