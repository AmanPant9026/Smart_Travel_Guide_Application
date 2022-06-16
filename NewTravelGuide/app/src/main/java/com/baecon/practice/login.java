package com.baecon.practice;

import android.content.Intent;
import android.os.Bundle;
import android.os.StrictMode;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import org.apache.http.NameValuePair;
import org.apache.http.message.BasicNameValuePair;
import org.json.JSONException;

import java.util.ArrayList;
import java.util.List;

import androidx.appcompat.app.AppCompatActivity;

public class login extends AppCompatActivity {
    public static String session = "";
    TextView txnew, txlog;
    EditText ed1,ed2;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        txnew = findViewById(R.id.newtx);
        txlog = findViewById(R.id.txlog);
        ed1 = findViewById(R.id.user);
        ed2 = findViewById(R.id.pass);

        txnew.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent io = new Intent(login.this,registration.class);
                startActivity(io);
            }
        });

        txlog.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String username = ed1.getText().toString();
                String password = ed2.getText().toString();

                if(username.equals("") || password.equals("")){
                    Toast.makeText(login.this, "Please fill details.", Toast.LENGTH_SHORT).show();
                }
                else {

                    StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
                    StrictMode.setThreadPolicy(policy);
                    String url = UrlLinks.pylogin;

                    List<NameValuePair> nameValuePairs = new ArrayList<NameValuePair>(2);

                    nameValuePairs.add(new BasicNameValuePair("username", username));
                    nameValuePairs.add(new BasicNameValuePair("password", password));

                    String result = null;
                    try {
                        result = jSOnClassforData.forCallingStringAndreturnSTring(url,nameValuePairs);
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }

                    if (result.equals("success")) {

                        session = username;
                        Toast.makeText(login.this, "Successfully", Toast.LENGTH_SHORT).show();
                        Intent io = new Intent(login.this, MainActivity.class);

                        startActivity(io);
                        finish();

                    } else {

                        Toast.makeText(login.this, "Wrong username or password", Toast.LENGTH_SHORT).show();

                    }
                }
            }
        });
    }
}