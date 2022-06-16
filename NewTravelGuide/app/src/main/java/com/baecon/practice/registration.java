package com.baecon.practice;

import android.content.Intent;
import android.os.Bundle;
import android.os.StrictMode;
import android.util.Patterns;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import org.apache.http.NameValuePair;
import org.apache.http.message.BasicNameValuePair;
import org.json.JSONException;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;

import androidx.appcompat.app.AppCompatActivity;

public class registration extends AppCompatActivity {

    TextView reg;
    EditText ed1,ed2,ed3,ed4;
    public static String userdata="";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registration);

        reg = findViewById(R.id.txreg);
        ed1 = findViewById(R.id.ed1);
        ed2 = findViewById(R.id.ed2);
        ed3 = findViewById(R.id.ed3);
        ed4 = findViewById(R.id.ed4);

        reg.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String username = ed1.getText().toString();
                String email = ed2.getText().toString();
                String mobile = ed3.getText().toString();
                String password = ed4.getText().toString();
                Pattern pattern = Patterns.EMAIL_ADDRESS;

                if(username.equals("") || email.equals("")|| mobile.equals("")|| password.equals("")){
                    Toast.makeText(registration.this, "Please fill details", Toast.LENGTH_SHORT).show();
                }
                else if(!pattern.matcher(email).matches()){
                    Toast.makeText(registration.this, "Please enter valid email", Toast.LENGTH_SHORT).show();
                }
                else if(mobile.length() != 10){
                    Toast.makeText(registration.this, "Please enter valid mobile number", Toast.LENGTH_SHORT).show();
                }
                else {

                    StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
                    StrictMode.setThreadPolicy(policy);
                    String url = UrlLinks.pyregister;

                    List<NameValuePair> nameValuePairs = new ArrayList<NameValuePair>(4);

                    nameValuePairs.add(new BasicNameValuePair("username", username));
                    nameValuePairs.add(new BasicNameValuePair("password", password));
                    nameValuePairs.add(new BasicNameValuePair("emailid", email));
                    nameValuePairs.add(new BasicNameValuePair("mobilenumber", mobile));

                    String result = null;
                    try {
                        result = jSOnClassforData.forCallingStringAndreturnSTring(url,nameValuePairs);
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }

                    if (result.equals("success")) {

                        Toast.makeText(registration.this, "User Added successfully", Toast.LENGTH_SHORT).show();
                        Intent io = new Intent(registration.this, login.class);

                        startActivity(io);
                        finish();

                    } else {

                        Toast.makeText(registration.this, "Wrong username or password", Toast.LENGTH_SHORT).show();

                    }
                }

            }
        });
    }
}