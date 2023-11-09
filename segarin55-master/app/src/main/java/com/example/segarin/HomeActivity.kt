package com.example.segarin

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.google.android.material.bottomnavigation.BottomNavigationView

class HomeActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_home)

        val bottomNavigationView: BottomNavigationView = findViewById(R.id.bottomNavigationView)
        bottomNavigationView.setOnNavigationItemSelectedListener { item ->
            when (item.itemId) {
                R.id.menu_home -> {
                    // Handle Home menu item selection
                    true
                }
                R.id.menu_search -> {
                    // Handle Search menu item selection
                    true
                }
                R.id.menu_scan -> {
                    // Handle Scan menu item selection
                    true
                }
                R.id.menu_favorites -> {
                    // Handle Favorites menu item selection
                    true
                }
                R.id.menu_profile -> {
                    // Handle Profile menu item selection
                    true
                }
                else -> false
            }
        }
    }
}