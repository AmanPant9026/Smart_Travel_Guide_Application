package com.baecon.practice.ui.Recreation;

import android.app.ProgressDialog;
import android.os.Bundle;
import android.os.StrictMode;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.EditText;
import android.widget.ImageButton;

import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.baecon.practice.ExampleAdapter1.RecreationAdapter;
import com.baecon.practice.ExampleItem1.Recreation;
import com.baecon.practice.R;
import com.baecon.practice.UrlLinks;
import com.baecon.practice.jSOnClassforData;
import com.baecon.practice.login;
import com.baecon.practice.ui.home.HomeViewModel;

import org.apache.http.NameValuePair;
import org.apache.http.message.BasicNameValuePair;
import org.json.JSONArray;
import org.json.JSONException;

import java.util.ArrayList;
import java.util.List;

public class Recreation_frag extends Fragment {

    EditText Searchtext;
    private RecreationAdapter adapter;
    ImageButton bt_mic;
    private List<Recreation> exampleList;
    private List<Recreation> examples;
    private HomeViewModel homeViewModel;
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View root = inflater.inflate(R.layout.fragment_recreation_frag, container, false);

        fillExampleList();
        this.Searchtext = (EditText) root.findViewById(R.id.search_input);
        this.Searchtext.addTextChangedListener(new TextWatcher() {
            public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2) {
            }

            public void onTextChanged(CharSequence charSequence, int i, int i1, int i2) {
            }

            public void afterTextChanged(Editable editable) {
                filterQuery(editable.toString());
            }
        });


        RecyclerView recyclerView = (RecyclerView) root.findViewById( R.id.RecyclerView);
        recyclerView.setHasFixedSize(true);
        RecyclerView.LayoutManager layoutManager = new LinearLayoutManager(getActivity());
        this.adapter = new RecreationAdapter(exampleList,getActivity());
        recyclerView.setLayoutManager(layoutManager);
        recyclerView.setAdapter(this.adapter);
        return root;
    }

    private void fillExampleList() {
        exampleList = new ArrayList();

        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        StrictMode.setThreadPolicy(policy);

        String url = UrlLinks.getRecreationData;

        List<NameValuePair> nameValuePairs = new ArrayList<NameValuePair>(1);
        nameValuePairs.add(new BasicNameValuePair("username", login.session));

        final ProgressDialog dialog= ProgressDialog.show(getActivity(),"Fetching data", "Please wait....",true);
        new Thread(new Runnable() {
            @Override
            public void run() {

                String result = null;
                try {
                    result = jSOnClassforData.forCallingStringAndreturnSTring(url, nameValuePairs);
                } catch (JSONException e) {
                    e.printStackTrace();
                }

                exampleList.clear();

                try {
                    JSONArray jsonArray = new JSONArray(result);
                    for (int i = 0; i < jsonArray.length(); i++) {

                        String restoImgId = String.valueOf(jsonArray.getJSONArray(i).getString(1));
                        String name = String.valueOf(jsonArray.getJSONArray(i).getString(2));
                        String rating = String.valueOf(jsonArray.getJSONArray(i).getString(3));
                        String type = String.valueOf(jsonArray.getJSONArray(i).getString(4));
                        String time = String.valueOf(jsonArray.getJSONArray(i).getString(5));
                        String phone = String.valueOf(jsonArray.getJSONArray(i).getString(6));
                        String address = String.valueOf(jsonArray.getJSONArray(i).getString(7));
                        String ur = String.valueOf(jsonArray.getJSONArray(i).getString(7));

//                        float f1 = Float.parseFloat(rating);

                        String[] img = restoImgId.split("\\.");

                        int idff = getActivity().getResources().getIdentifier(img[0], "drawable", getActivity().getPackageName());

                        exampleList.add(new Recreation(idff, name, rating, type, phone, time, address, url));

//                        Thread.sleep(2000);
                        dialog.dismiss();
                    }
                } catch (JSONException e) {
                    e.printStackTrace();
                }

            }
        }).start();

    }

    /* access modifiers changed from: private */
    public void filterQuery(String text) {
        ArrayList<Recreation> filterdNames = new ArrayList<>();
        for (Recreation s : exampleList) {
            if (s.getRestaurantTitle().toLowerCase().contains(text) || s.getRestaurantRating().toLowerCase().contains(text)) {
                filterdNames.add(s);
            }
        }
        this.adapter.setFilter(filterdNames);
    }
}