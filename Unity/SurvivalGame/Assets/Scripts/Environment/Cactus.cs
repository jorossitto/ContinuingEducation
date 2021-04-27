using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Cactus : MonoBehaviour
{
    public int damage = 1;
    public float damageRate = 1;

    private List<IDamageable> thingsToDamage = new List<IDamageable>();

    private void Start()
    {
        StartCoroutine(DealDamage());
    }

    public IEnumerator DealDamage()
    {
        Debug.Log("Lets start dealing damage " + damage);
        while (true)
        {
            for(int i = 0; i < thingsToDamage.Count; i++)
            {
                Debug.Log("Take Damage " + damage);
                thingsToDamage[i].TakePhysicalDamage(damage);
            }
            yield return new WaitForSeconds(damageRate);
        }
    }

    private void OnCollisionEnter(Collision collision)
    {
        Debug.Log("You collided with me");
        if(collision.gameObject.GetComponent<IDamageable>() != null)
        {
            thingsToDamage.Add(collision.gameObject.GetComponent<IDamageable>());
        }
    }

    private void OnCollisionExit(Collision collision)
    {
        if (collision.gameObject.GetComponent<IDamageable>() != null)
        {
            thingsToDamage.Remove(collision.gameObject.GetComponent<IDamageable>());
        }
    }
}
