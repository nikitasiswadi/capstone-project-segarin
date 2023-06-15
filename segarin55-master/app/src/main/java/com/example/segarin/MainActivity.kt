package com.example.segarin

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.content.Context
import android.content.Intent
import android.content.SharedPreferences
import android.widget.Button
import android.widget.EditText

//import kotlinx.android.synthetic.main.activity_login.*

class MainActivity : AppCompatActivity() {
    private lateinit var sharedPreferences: SharedPreferences

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        sharedPreferences = getSharedPreferences("MY_PRE", Context.MODE_PRIVATE)

        findViewById<Button>(R.id.loginButton).setOnClickListener {
            val enteredUsername = findViewById<EditText>(R.id.emailEditText).text.toString()
            val enteredPassword = findViewById<EditText>(R.id.passwordEditText).text.toString()

            val editor = sharedPreferences.edit()
            editor.putString("USERNAME", enteredUsername)
            editor.putString("PASSWORD", enteredPassword)
            editor.apply()

            val i = Intent(this, HomeActivity::class.java)
            startActivity(i)
//            val storedUsername = sharedPreferences.getString("username", "")
//            val storedPassword = sharedPreferences.getString("password", "")
//
//            if (enteredUsername == storedUsername && enteredPassword == storedPassword) {
//                // Credentials match, user is logged in
//                // You can start a new activity or perform other operations here
//            } else {
//                // Credentials do not match, show an error message
//            }
        }
    }
}