using Cinemachine;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraHandler : MonoBehaviour
{
    public static CameraHandler Instance { get; private set; }



    [SerializeField] private CinemachineVirtualCamera cinemachineVirtualCamera;

    private float ortographicSize;
    private float targetOrtographicSize;
    private bool edgeScrolling;

    private void Awake()
    {
        Instance = this;

        edgeScrolling = PlayerPrefs.GetInt("edgeScrolling", 1) == 1;
    }

    private void Start()
    {
        ortographicSize = cinemachineVirtualCamera.m_Lens.OrthographicSize;
        targetOrtographicSize = ortographicSize;
    }
    private void Update()
    {
        float x = Input.GetAxisRaw("Horizontal");
        float y = Input.GetAxisRaw("Vertical");


        if (edgeScrolling)
        {
            float edgeScrollingSize = 30;
            if (Input.mousePosition.x > Screen.width - edgeScrollingSize)
            {
                x = +1f;
            }
            if (Input.mousePosition.x < edgeScrollingSize)
            {
                x = -1f;
            }
            if (Input.mousePosition.y > Screen.height - edgeScrollingSize)
            {
                y = +1f;
            }
            if (Input.mousePosition.y < edgeScrollingSize)
            {
                y = -1f;
            }
        }
        Vector3 moveDir = new Vector3 (x, y).normalized;
        float moveSpeed = 30f;

        transform.position += moveDir * moveSpeed * Time.deltaTime;

        float zoomAmount = 2f;
        targetOrtographicSize += -Input.mouseScrollDelta.y * zoomAmount;

        float minOrtographicSize = 5; // zoom in
        float maxOrtographicSize = 25; // zoom out
        targetOrtographicSize = Mathf.Clamp(targetOrtographicSize, minOrtographicSize, maxOrtographicSize);

        float zoomSpeed = 10f;
        ortographicSize = Mathf.Lerp(ortographicSize, targetOrtographicSize, Time.deltaTime * zoomSpeed); 

        cinemachineVirtualCamera.m_Lens.OrthographicSize = ortographicSize;
    }

    public void SetEdgeScrolling (bool edgeScrolling)
    {
        this.edgeScrolling = edgeScrolling;
        PlayerPrefs.SetInt("edgeScrolling", edgeScrolling ? 1 : 0);
    }

    public bool GetEdgeScrolling()
    {
        return edgeScrolling;
    }
}
