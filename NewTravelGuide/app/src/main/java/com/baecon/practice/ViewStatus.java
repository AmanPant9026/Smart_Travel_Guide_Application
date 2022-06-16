package com.baecon.practice;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.os.Bundle;
import android.os.StrictMode;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Switch;
import android.widget.TextView;
import android.widget.Toast;

import org.apache.http.NameValuePair;
import org.apache.http.message.BasicNameValuePair;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.json.XML;

import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;


public class ViewStatus extends AppCompatActivity {

    TextView tx,comname,ipadd,methodname,formatname;
    Switch sw1,sw2,sw3,sw4;
    String name;
    public static String companyname;
    public static String ipaddress;
    public static String method;
    public static String format;
    public static String fan;
    public static String ac;
    public static String light;
    public static String freeze;

    Button b1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_status);

        String data = getIntent().getStringExtra("data");
        tx = findViewById(R.id.txlog);

        String firstFourChars = data.substring(0, 5);

        name = data;
        if(!firstFourChars.equals("{\"com")){
            JSONObject jsonObj = null;
            try {
                jsonObj = XML.toJSONObject(data);
                name = jsonObj.getString("Data");
            } catch (JSONException e) {
                Log.e("JSON exception", e.getMessage());
                e.printStackTrace();
            }
        }

        try {
            JSONObject jsonObj = new JSONObject(name);
            companyname = jsonObj.getString("company");
            ipaddress = jsonObj.getString("ip");
            method = jsonObj.getString("method");
            format = jsonObj.getString("formats");
            fan = jsonObj.getString("fan");
            ac = jsonObj.getString("ac");
            light = jsonObj.getString("light");
            freeze = jsonObj.getString("freeze");
        } catch (JSONException e) {
            e.printStackTrace();
        }

        comname = findViewById(R.id.companyname);
        ipadd = findViewById(R.id.ipaddname);
        methodname = findViewById(R.id.methodname);
        formatname = findViewById(R.id.formatname);
        sw1 = findViewById(R.id.fan);
        sw2 = findViewById(R.id.Ac);
        sw3 = findViewById(R.id.Light);
        sw4 = findViewById(R.id.Freeze);

        comname.setText(companyname);
        ipadd.setText(ipaddress);
        methodname.setText(method);
        formatname.setText(format);
        sw1.setChecked(Boolean.parseBoolean(fan));
        sw2.setChecked(Boolean.parseBoolean(ac));
        sw3.setChecked(Boolean.parseBoolean(light));
        sw4.setChecked(Boolean.parseBoolean(freeze));

        b1 = findViewById(R.id.btn);

        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String fan = String.valueOf(sw1.isChecked());
                String ac = String.valueOf(sw2.isChecked());
                String light = String.valueOf(sw3.isChecked());
                String freeze = String.valueOf(sw4.isChecked());

                if(format.equals("JSON")){

                    String datastr = "{\"company\": \""+companyname+"\", \"ip\": \""+ipaddress+"\", \"method\": \""+method+"\", \"formats\": \""+format+"\", \"fan\": \""+fan+"\", \"ac\": \""+ac+"\", \"light\": \""+light+"\", \"freeze\": \""+freeze+"\"}";

                    StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
                    StrictMode.setThreadPolicy(policy);
                    String url = UrlLinks.api;

                    List<NameValuePair> nameValuePairs = new ArrayList<NameValuePair>(1);

                    nameValuePairs.add(new BasicNameValuePair("company", datastr));

                    String result = null;
                    try {
                        result = jSOnClassforData.forCallingStringAndreturnSTring(url, nameValuePairs);
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }

                    Toast.makeText(ViewStatus.this, result, Toast.LENGTH_SHORT).show();

                }
                else {

                    String stryys = "<Data company=\""+companyname+"\" ip=\""+ipaddress+"\" method=\""+method+"\" formats=\""+format+"\" fan=\""+fan+"\" ac=\""+ac+"\" light=\""+light+"\" freeze=\""+freeze+"\" />";

                    StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
                    StrictMode.setThreadPolicy(policy);
                    String url = UrlLinks.api;

                    List<NameValuePair> nameValuePairs = new ArrayList<NameValuePair>(1);

                    nameValuePairs.add(new BasicNameValuePair("company", stryys));

                    String result = null;
                    try {
                        result = jSOnClassforData.forCallingStringAndreturnSTring(url, nameValuePairs);
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }

                    Toast.makeText(ViewStatus.this, result, Toast.LENGTH_SHORT).show();

                }

            }
        });


    }
}