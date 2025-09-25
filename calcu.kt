package com.example.calculadorainteractiva

import android.animation.ArgbEvaluator
import android.animation.ObjectAnimator
import android.animation.ValueAnimator
import android.content.Context
import android.graphics.Color
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.text.Editable
import android.text.TextWatcher
import android.view.View
import android.view.animation.AccelerateDecelerateInterpolator
import android.widget.*
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import java.text.SimpleDateFormat
import java.util.*
import kotlin.math.pow
import kotlin.math.sqrt
import kotlin.random.Random

class MainActivity : AppCompatActivity() {
    
    // UI Components
    private lateinit var etNumero1: EditText
    private lateinit var etNumero2: EditText
    private lateinit var tvResultado: TextView
    private lateinit var tvTitulo: TextView
    private lateinit var lvHistorial: ListView
    private lateinit var tvBarraEstado: TextView
    private lateinit var scrollView: ScrollView
    
    // Botones
    private lateinit var btnSumar: Button
    private lateinit var btnRestar: Button
    private lateinit var btnMultiplicar: Button
    private lateinit var btnDividir: Button
    private lateinit var btnPotencia: Button
    private lateinit var btnRaiz: Button
    private lateinit var btnRandom: Button
    private lateinit var btnCambiarTema: Button
    private lateinit var btnLimpiarHistorial: Button
    
    // Variables
    private val historial = mutableListOf<String>()
    private lateinit var historialAdapter: ArrayAdapter<String>
    private var temaActual = 0
    private val handler = Handler(Looper.getMainLooper())
    private lateinit var actualizadorHora: Runnable
    
    // Temas de colores
    private val temas = listOf(
        Tema("#2C3E50", "#ECF0F1", "#3498DB"),
        Tema("#8E44AD", "#F8F9FA", "#E74C3C"),
        Tema("#27AE60", "#FFFFFF", "#F39C12"),
        Tema("#34495E", "#BDC3C7", "#E67E22")
    )
    
    data class Tema(val fondo: String, val texto: String, val boton: String)
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        inicializarComponentes()
        configurarEventos()
        configurarHistorial()
        aplicarTema()
        mostrarMensajeBienvenida()
        iniciarActualizadorHora()
    }
    
    private fun inicializarComponentes() {
        // EditTexts
        etNumero1 = findViewById(R.id.etNumero1)
        etNumero2 = findViewById(R.id.etNumero2)
        
        // TextViews
        tvResultado = findViewById(R.id.tvResultado)
        tvTitulo = findViewById(R.id.tvTitulo)
        tvBarraEstado = findViewById(R.id.tvBarraEstado)
        
        // ListView para historial
        lvHistorial = findViewById(R.id.lvHistorial)
        
        // Botones operaciones básicas
        btnSumar = findViewById(R.id.btnSumar)
        btnRestar = findViewById(R.id.btnRestar)
        btnMultiplicar = findViewById(R.id.btnMultiplicar)
        btnDividir = findViewById(R.id.btnDividir)
        
        // Botones especiales
        btnPotencia = findViewById(R.id.btnPotencia)
        btnRaiz = findViewById(R.id.btnRaiz)
        btnRandom = findViewById(R.id.btnRandom)
        btnCambiarTema = findViewById(R.id.btnCambiarTema)
        btnLimpiarHistorial = findViewById(R.id.btnLimpiarHistorial)
        
        scrollView = findViewById(R.id.scrollView)
    }
    
    private fun configurarEventos() {
        // Eventos de botones de operaciones
        btnSumar.setOnClickListener { realizarOperacion(Operacion.SUMA) }
        btnRestar.setOnClickListener { realizarOperacion(Operacion.RESTA) }
        btnMultiplicar.setOnClickListener { realizarOperacion(Operacion.MULTIPLICACION) }
        btnDividir.setOnClickListener { realizarOperacion(Operacion.DIVISION) }
        btnPotencia.setOnClickListener { realizarOperacion(Operacion.POTENCIA) }
        btnRaiz.setOnClickListener { realizarOperacion(Operacion.RAIZ_CUADRADA) }
        
        // Eventos especiales
        btnRandom.setOnClickListener { generarNumeroRandom() }
        btnCambiarTema.setOnClickListener { cambiarTema() }
        btnLimpiarHistorial.setOnClickListener { limpiarHistorial() }
        
        // Efectos en EditTexts
        configurarEfectosEntrada(etNumero1)
        configurarEfectosEntrada(etNumero2)
        
        // Efectos hover en botones
        configurarEfectosHover()
    }
    
    private fun configurarEfectosEntrada(editText: EditText) {
        editText.addTextChangedListener(object : TextWatcher {
            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {}
            override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {}
            override fun afterTextChanged(s: Editable?) {
                if (s?.isNotEmpty() == true) {
                    editText.setBackgroundColor(Color.parseColor("#D5DBDB"))
                } else {
                    editText.setBackgroundColor(Color.WHITE)
                }
            }
        })
    }
    
    private fun configurarEfectosHover() {
        val botones = listOf(btnSumar, btnRestar, btnMultiplicar, btnDividir, 
                           btnPotencia, btnRaiz, btnRandom, btnCambiarTema)
        
        botones.forEach { boton ->
            boton.setOnTouchListener { v, event ->
                when (event.action) {
                    android.view.MotionEvent.ACTION_DOWN -> {
                        animarBoton(v as Button, true)
                    }
                    android.view.MotionEvent.ACTION_UP, android.view.MotionEvent.ACTION_CANCEL -> {
                        animarBoton(v as Button, false)
                    }
                }
                false
            }
        }
    }
    
    private fun animarBoton(boton: Button, presionado: Boolean) {
        val escala = if (presionado) 0.95f else 1.0f
        val alpha = if (presionado) 0.8f else 1.0f
        
        boton.animate()
            .scaleX(escala)
            .scaleY(escala)
            .alpha(alpha)
            .setDuration(100)
            .start()
    }
    
    private fun configurarHistorial() {
        historialAdapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, historial)
        lvHistorial.adapter = historialAdapter
    }
    
    enum class Operacion {
        SUMA, RESTA, MULTIPLICACION, DIVISION, POTENCIA, RAIZ_CUADRADA
    }
    
    private fun realizarOperacion(operacion: Operacion) {
        val (num1, num2, valido) = obtenerNumeros()
        if (!valido) return
        
        try {
            val resultado = when (operacion) {
                Operacion.SUMA -> {
                    val res = num1 + num2
                    mostrarResultado(res, "$num1 + $num2")
                    res
                }
                Operacion.RESTA -> {
                    val res = num1 - num2
                    mostrarResultado(res, "$num1 - $num2")
                    res
                }
                Operacion.MULTIPLICACION -> {
                    val res = num1 * num2
                    mostrarResultado(res, "$num1 × $num2")
                    res
                }
                Operacion.DIVISION -> {
                    if (num2 == 0.0) {
                        mostrarError("¡No se puede dividir por cero!")
                        explosionError()
                        return
                    }
                    val res = num1 / num2
                    mostrarResultado(res, "$num1 ÷ $num2")
                    res
                }
                Operacion.POTENCIA -> {
                    val res = num1.pow(num2)
                    if (res.isInfinite() || res.isNaN()) {
                        mostrarAdvertencia("Resultado demasiado grande")
                        return
                    }
                    mostrarResultado(res, "$num1 ^ $num2")
                    res
                }
                Operacion.RAIZ_CUADRADA -> {
                    if (num1 < 0) {
                        mostrarError("No se puede calcular raíz de número negativo")
                        return
                    }
                    val res = sqrt(num1)
                    mostrarResultado(res, "√$num1")
                    res
                }
            }
        } catch (e: Exception) {
            mostrarError("Error en el cálculo: ${e.message}")
        }
    }
    
    private data class ResultadoNumeros(val num1: Double, val num2: Double, val valido: Boolean)
    
    private fun obtenerNumeros(): ResultadoNumeros {
        return try {
            val num1 = if (etNumero1.text.toString().isNotEmpty()) {
                etNumero1.text.toString().toDouble()
            } else 0.0
            
            val num2 = if (etNumero2.text.toString().isNotEmpty()) {
                etNumero2.text.toString().toDouble()
            } else 0.0
            
            ResultadoNumeros(num1, num2, true)
        } catch (e: NumberFormatException) {
            mostrarError("Por favor, ingrese números válidos")
            ResultadoNumeros(0.0, 0.0, false)
        }
    }
    
    private fun mostrarResultado(resultado: Double, operacion: String) {
        // Formatear resultado
        val resultadoFormateado = if (resultado % 1.0 == 0.0) {
            resultado.toInt().toString()
        } else {
            String.format("%.6f", resultado).trimEnd('0').trimEnd('.')
        }
        
        tvResultado.text = resultadoFormateado
        tvResultado.setBackgroundColor(Color.parseColor("#27AE60"))
        tvResultado.setTextColor(Color.WHITE)
        
        agregarHistorial(operacion, resultadoFormateado)
        animarResultado()
        mostrarMensajeExito(resultadoFormateado)
    }
    
    private fun agregarHistorial(operacion: String, resultado: String) {
        val timestamp = SimpleDateFormat("HH:mm:ss", Locale.getDefault()).format(Date())
        val entrada = "[$timestamp] $operacion = $resultado"
        historial.add(0, entrada) // Agregar al inicio
        historialAdapter.notifyDataSetChanged()
        
        // Limitar historial a 50 entradas
        if (historial.size > 50) {
            historial.removeAt(historial.size - 1)
        }
    }
    
    private fun animarResultado() {
        val colores = intArrayOf(
            Color.parseColor("#27AE60"),
            Color.parseColor("#2ECC71"),
            Color.parseColor("#27AE60"),
            Color.parseColor("#58D68D")
        )
        
        val animator = ValueAnimator.ofInt(*colores)
        animator.setEvaluator(ArgbEvaluator())
        animator.duration = 800
        animator.addUpdateListener { animation ->
            tvResultado.setBackgroundColor(animation.animatedValue as Int)
        }
        animator.start()
    }
    
    private fun generarNumeroRandom() {
        val numero = Random.nextInt(1, 1001)
        etNumero1.setText(numero.toString())
        
        // Animación del EditText
        etNumero1.animate()
            .scaleX(1.1f)
            .scaleY(1.1f)
            .setDuration(200)
            .withEndAction {
                etNumero1.animate()
                    .scaleX(1.0f)
                    .scaleY(1.0f)
                    .setDuration(200)
                    .start()
            }
            .start()
        
        mostrarInfo("🎲 Número Random", "¡Número generado: $numero!")
    }
    
    private fun cambiarTema() {
        temaActual = (temaActual + 1) % temas.size
        aplicarTema()
        mostrarInfo("🎨 Tema Cambiado", "¡Nuevo tema aplicado!")
    }
    
    private fun aplicarTema() {
        val tema = temas[temaActual]
        
        // Aplicar colores de fondo
        findViewById<View>(R.id.mainLayout).setBackgroundColor(Color.parseColor(tema.fondo))
        
        // Aplicar colores de texto
        tvTitulo.setTextColor(Color.parseColor(tema.texto))
        tvBarraEstado.setBackgroundColor(Color.parseColor("#34495E"))
        
        // Aplicar colores a botones especiales
        val botonesEspeciales = listOf(btnPotencia, btnRaiz, btnRandom, btnCambiarTema)
        botonesEspeciales.forEach { boton ->
            boton.setBackgroundColor(Color.parseColor(tema.boton))
        }
    }
    
    private fun limpiarHistorial() {
        AlertDialog.Builder(this)
            .setTitle("🗑️ Limpiar Historial")
            .setMessage("¿Está seguro de limpiar el historial?")
            .setPositiveButton("Sí") { _, _ ->
                historial.clear()
                historialAdapter.notifyDataSetChanged()
                mostrarInfo("✅ Limpio", "Historial limpiado exitosamente")
            }
            .setNegativeButton("No", null)
            .show()
    }
    
    private fun explosionError() {
        val colores = intArrayOf(
            Color.RED,
            Color.parseColor(temas[temaActual].texto)
        )
        
        repeat(5) { i ->
            handler.postDelayed({
                tvTitulo.setTextColor(colores[i % 2])
            }, (i * 200).toLong())
        }
    }
    
    private fun mostrarMensajeExito(resultado: String) {
        val mensajes = listOf(
            "¡Excelente! El resultado es $resultado 🎉",
            "¡Perfecto! Has calculado $resultado ⭐",
            "¡Increíble! La respuesta es $resultado 🚀",
            "¡Fantástico! Obtuviste $resultado 💫"
        )
        
        val mensaje = mensajes.random()
        tvBarraEstado.text = mensaje
        
        handler.postDelayed({
            actualizarBarraEstado()
        }, 3000)
    }
    
    private fun iniciarActualizadorHora() {
        actualizadorHora = object : Runnable {
            override fun run() {
                actualizarBarraEstado()
                handler.postDelayed(this, 1000)
            }
        }
        handler.post(actualizadorHora)
    }
    
    private fun actualizarBarraEstado() {
        val hora = SimpleDateFormat("HH:mm:ss", Locale.getDefault()).format(Date())
        if (tvBarraEstado.text.contains("Calculadora lista") || 
            tvBarraEstado.text.length < 50) {
            tvBarraEstado.text = "Calculadora lista • $hora"
        }
    }
    
    private fun mostrarMensajeBienvenida() {
        AlertDialog.Builder(this)
            .setTitle("🎉 ¡Bienvenido!")
            .setMessage(
                "¡Bienvenido a la Calculadora Súper Interactiva!\n\n" +
                        "✨ Características:\n" +
                        "• Operaciones básicas y avanzadas\n" +
                        "• Historial de operaciones\n" +
                        "• Múltiples temas de colores\n" +
                        "• Efectos visuales y animaciones\n" +
                        "• ¡Y mucho más!\n\n" +
                        "¡Disfruta calculando! 🧮"
            )
            .setPositiveButton("¡Empezar!") { dialog, _ ->
                dialog.dismiss()
            }
            .setCancelable(false)
            .show()
    }
    
    private fun mostrarError(mensaje: String) {
        AlertDialog.Builder(this)
            .setTitle("❌ Error")
            .setMessage(mensaje)
            .setPositiveButton("OK", null)
            .show()
    }
    
    private fun mostrarAdvertencia(mensaje: String) {
        AlertDialog.Builder(this)
            .setTitle("⚠️ Advertencia")
            .setMessage(mensaje)
            .setPositiveButton("OK", null)
            .show()
    }
    
    private fun mostrarInfo(titulo: String, mensaje: String) {
        AlertDialog.Builder(this)
            .setTitle(titulo)
            .setMessage(mensaje)
            .setPositiveButton("OK", null)
            .show()
    }
    
    override fun onDestroy() {
        super.onDestroy()
        handler.removeCallbacks(actualizadorHora)
    }
}