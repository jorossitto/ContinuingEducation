using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.UI;
using UnityEngine.InputSystem;
using UnityEngine.Events;

public class Inventory : MonoBehaviour
{
    public ItemSlotsUI[] UISlots;
    public ItemSlot[] slots;

    public GameObject inventoryWindow;
    public Transform dropPosition;

    [Header("Selected Item")]
    private ItemSlot selectedItem;
    private int selectedItemIndex;

    public TextMeshProUGUI selectedItemName;
    public TextMeshProUGUI selectedDescription;
    public TextMeshProUGUI selectedItemStatNames;
    public TextMeshProUGUI selectedItemStatValues;

    public GameObject useButton;
    public GameObject equipButton;
    public GameObject unEquipButton;
    public GameObject dropButton;

    private int curEquipIndex;

    //components
    private PlayerController controller;

    [Header("Events")]
    public UnityEvent onOpenInventory;
    public UnityEvent onCloseInventory;

    public static Inventory instance;

    private void Awake()
    {
        instance = this;
        controller = GetComponent<PlayerController>();

    }

    private void Start()
    {
        inventoryWindow.SetActive(false);
        slots = new ItemSlot[UISlots.Length];

        //initalize the slots
        for(int x = 0; x < slots.Length; x++)
        {
            slots[x] = new ItemSlot();
            UISlots[x].index = x;
            UISlots[x].Clear();
        }
    }

    public void Toggle()
    {

    }

    public bool IsOpen()
    {
        return inventoryWindow.activeInHierarchy;
    }

    public void AddItem(ItemData item)
    {
        if(item.canStack)
        {
            ItemSlot slotToStackTo = GetItemStack(item);
            if(slotToStackTo != null)
            {
                slotToStackTo.quantity++;
                UpdateUI();
                return;
            }
        }

        ItemSlot emptySlot = GetEmptySlot();
        if(emptySlot != null)
        {
            emptySlot.item = item;
            emptySlot.quantity = 1;
            UpdateUI();
            return;
        }

        //If the item can not find a slot throw the item away
        ThrowItem(item);
    }

    void ThrowItem(ItemData item)
    {

    }

    void UpdateUI()
    {
        for(int x = 0; x < slots.Length; x++)
        {

        }
    }

    ItemSlot GetItemStack(ItemData item)
    {
        return null;
    }

    ItemSlot GetEmptySlot()
    {
        return null;
    }

    public void SelectItem (int index)
    {

    }

    void ClearSelectedItemWindow()
    {

    }
    public void OnUsebutton()
    {

    }

    public void OnEquipButton()
    {

    }

    void UnEquip(int index)
    {

    }

    public void OnUnequipButton()
    {

    }
    public void OnDropButton()
    {

    }

    void RemoveSelectedItem()
    {

    }

    public void RemoveItem(ItemData item)
    {

    }

    public bool HasItems(ItemData item, int quantity)
    {
        return false;
    }

}

public class ItemSlot
{
    public ItemData item;
    public int quantity;
}
