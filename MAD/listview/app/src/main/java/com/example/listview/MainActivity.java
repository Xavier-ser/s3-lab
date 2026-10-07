package com.example.listview;

import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    ListView lv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        lv = findViewById(R.id.lv);

        String[] names = {
                "Aarjav",
                "Abhay",
                "Jithu",
                "aravindh",
                "Nandana"
        };

        ArrayAdapter<String> adapter =
                new ArrayAdapter<>(
                        this,
                        android.R.layout.simple_list_item_1,
                        names
                );

        lv.setAdapter(adapter);

        lv.setOnItemClickListener((parent, view, position, id) -> {

            String selectedName = names[position];

            Toast.makeText(
                    MainActivity.this,
                    "Name Clicked: " + selectedName,
                    Toast.LENGTH_SHORT
            ).show();
        });
    }
}