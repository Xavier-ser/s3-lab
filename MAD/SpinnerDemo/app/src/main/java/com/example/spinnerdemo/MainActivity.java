package com.example.spinnerdemo;

import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Spinner;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    Spinner s;
    TextView t1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        s = findViewById(R.id.sp);
        t1 = findViewById(R.id.t1);

        ArrayList<String> fruits = new ArrayList<>();

        fruits.add("mango");
        fruits.add("apple");
        fruits.add("pineapple");
        fruits.add("banana");

        ArrayAdapter<String> adapter =
                new ArrayAdapter<>(
                        this,
                        android.R.layout.simple_spinner_dropdown_item,
                        fruits
                );

        s.setAdapter(adapter);

        s.setOnItemSelectedListener(
                new AdapterView.OnItemSelectedListener() {

                    @Override
                    public void onItemSelected(
                            AdapterView<?> parent,
                            View view,
                            int position,
                            long id) {

                        t1.setText(
                                "Selected Fruit: " + fruits.get(position)
                        );
                    }

                    @Override
                    public void onNothingSelected(
                            AdapterView<?> parent) {

                        t1.setText("Select a Fruit !!!!");
                    }
                }
        );
    }
}