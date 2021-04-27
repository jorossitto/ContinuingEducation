using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Events;

public class PlayerNeeds : MonoBehaviour, IDamageable
{
    public Need health;
    public Need hunger;
    public Need thirst;
    public Need sleep;

    public float noHungerHealthDecay;
    public float noThirstHealthDecay;

    public UnityEvent onTakeDamage;

    private void Start()
    {
        health.currentValue = health.startValue;
        hunger.currentValue = hunger.startValue;
        thirst.currentValue = thirst.startValue;
        sleep.currentValue = sleep.startValue;
    }
    private void Update()
    {
        //decay needs over time
        hunger.Subtract(hunger.decayRate * Time.deltaTime);
        thirst.Subtract(thirst.decayRate * Time.deltaTime);
        sleep.Add(sleep.regenRate * Time.deltaTime);

        if(hunger.currentValue == 0.0f)
        {
            health.Subtract(noHungerHealthDecay * Time.deltaTime);
        }
        if(thirst.currentValue == 0.0f)
        {
            health.Subtract(noThirstHealthDecay * Time.deltaTime);
        }

        //check if player is dead
        if(health.currentValue == 0.0f)
        {
            Die();
        }

        //update UI
        health.uiBar.fillAmount = health.GetPercentage();
        hunger.uiBar.fillAmount = hunger.GetPercentage();
        thirst.uiBar.fillAmount = thirst.GetPercentage();
        sleep.uiBar.fillAmount = sleep.GetPercentage();

    }

    public void Heal(float amount)
    {
        health.Add(amount);
    }
    public void Eat(float amount)
    {
        hunger.Add(amount);
    }
    public void Drink(float amount)
    {
        thirst.Add(amount);
    }
    public void Sleep(float amount)
    {
        sleep.Subtract(amount);
    }
    public void TakePhysicalDamage(int amount)
    {
        health.Subtract(amount);
        onTakeDamage?.Invoke();
    }
    public void Die()
    {
        Debug.Log("Player is dead");
    }
}

[System.Serializable]
public class Need
{
    [HideInInspector]
    public float currentValue;
    public float maxValue;
    public float startValue;
    public float regenRate;
    public float decayRate;
    public Image uiBar;

    public void Add (float amount)
    {
        currentValue = Mathf.Min(currentValue + amount, maxValue);
    }

    public void Subtract(float amount)
    {
        currentValue = Mathf.Max(currentValue - amount, 0.0f);
    }

    public float GetPercentage()
    {
        return currentValue / maxValue;
    }
}

public interface IDamageable
{
    void TakePhysicalDamage(int damageAmount);
}
