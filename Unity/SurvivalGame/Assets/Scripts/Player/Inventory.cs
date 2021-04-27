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
    private bool isEquipable;
    private bool isEquipped;
    private bool isConsumable;

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

        ClearSelectedItemWindow();
    }

    public void OnInventoryButton(InputAction.CallbackContext context)
    {
        if(context.phase == InputActionPhase.Started)
        {
            Toggle();
        }

    }
    public void Toggle()
    {
        if(inventoryWindow.activeInHierarchy)
        {
            inventoryWindow.SetActive(false);
            onCloseInventory.Invoke();
        }
        else
        {
            inventoryWindow.SetActive(true);
            onOpenInventory.Invoke();
            ClearSelectedItemWindow();
        }
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

    //spawns item in front of the player
    void ThrowItem(ItemData item)
    {
        Instantiate(item.dropPrefab, dropPosition.position, Quaternion.Euler(Vector3.one * Random.value * 360.0f));
    }

    void UpdateUI()
    {
        for(int x = 0; x < slots.Length; x++)
        {
            if(slots[x].item != null)
            {
                UISlots[x].Set(slots[x]);
            }
            else
            {
                UISlots[x].Clear();
            }
        }
    }

    ItemSlot GetItemStack(ItemData item)
    {
        for(int x = 0; x < slots.Length; x++)
        {
            if(slots[x].item == item && slots[x].quantity < item.maxStackAmount)
            {
                return slots[x];
            }
        }
        return null;
    }

    //returns an empty slot in the inventory
    //if there are no empty slots - return null
    ItemSlot GetEmptySlot()
    {
        for(int x = 0; x < slots.Length; x++)
        {
            if(slots[x].item == null)
            {
                return slots[x];
            }
        }
        return null;
    }

    public void SelectItem (int index)
    {
        if(slots[index].item == null)
        {
            return;
        }

        selectedItem = slots[index];
        selectedItemIndex = index;
        selectedItemName.text = selectedItem.item.displayName;
        selectedDescription.text = selectedItem.item.description;

        //todo set stat values and stat names


        isConsumable = selectedItem.item.type == ItemType.Consumable;
        isEquipable = selectedItem.item.type == ItemType.Equipable;
        isEquipped = UISlots[index].equipped;

        useButton.SetActive(isConsumable);
        equipButton.SetActive(isEquipable && !isEquipped);
        unEquipButton.SetActive(isEquipable && isEquipped);
        dropButton.SetActive(true);
    }

    void ClearSelectedItemWindow()
    {
        //clear text elements
        selectedItem = null;
        selectedItemName.text = string.Empty;
        selectedDescription.text = string.Empty;
        selectedItemStatNames.text = string.Empty;
        selectedItemStatValues.text = string.Empty;

        //disable buttons
        useButton.SetActive(false);
        equipButton.SetActive(false);
        unEquipButton.SetActive(false);
        dropButton.SetActive(false);
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
