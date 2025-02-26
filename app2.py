import streamlit as st

def main():
    st.set_page_config(page_title="Virtual Machines and Memory Virtualization", layout="wide")  # Changed to wide layout

    # Sidebar with dropdown for terminology search
    st.sidebar.header("Terminology Search")
    terminology = {
        "Cache Coherence": "Ensures all CPU caches maintain a consistent view of memory.",
    "Full Virtualization": "A method where the VMM completely emulates hardware so that an unmodified guest OS can run.",
    "Hardware-Assisted Virtualization": "CPU features that provide direct support for virtualization, reducing the need for software-based emulation (e.g., Intel VT-x, AMD-V).",
    "Host OS vs. Guest OS": "The host OS is the primary operating system running on the physical machine, while the guest OS runs within a virtual machine.",
    "Live Migration": "The process of moving a running VM from one physical host to another without downtime.",
    "Memory Management Unit (MMU)": "A hardware component that translates virtual addresses into physical addresses.",
    "Page Fault": "Occurs when a requested page is not in physical memory, requiring the OS to fetch it from disk.",
    "Page Table": "A data structure used by the OS to map virtual addresses to physical addresses.",
    "Paging": "A memory management scheme that divides virtual memory into fixed-size units called pages.",
    "Paravirtualization": "A virtualization method where the guest OS is modified to work efficiently with the hypervisor.",
    "Resource Sharing": "Multiple VMs share hardware resources such as CPU, memory, and storage, improving utilization.",
    "Snooping Protocol": "A cache coherence mechanism where caches monitor the bus for changes.",
    "Trap-and-Emulate": "A method where the VMM intercepts privileged instructions executed by the guest OS and safely emulates them.",
    "Translation Lookaside Buffer (TLB)": "A cache that stores recent virtual-to-physical address mappings to speed up address translation.",
    "Type 1 Hypervisor (Bare Metal)": "Runs directly on the hardware without a host OS (e.g., VMware ESXi, Microsoft Hyper-V, Xen).",
    "Type 2 Hypervisor (Hosted)": "Runs on a conventional operating system and manages VMs as applications (e.g., VMware Workstation, VirtualBox).",
    "Virtual Machines (VMs)": "A software emulation of a physical computer system, allowing multiple operating systems to run on the same hardware.",
    "Virtual Memory": "A system where the OS uses disk storage to extend RAM, allowing processes to use more memory than is physically available.",
    "Virtual Machine Monitor (VMM) / Hypervisor": "A software layer that manages virtual machines by mapping virtual resources to physical resources.",
    "VM Isolation": "The principle that each VM is independent and cannot directly interfere with others, improving security and reliability.",
    "VM Snapshots": "A saved state of a virtual machine that can be restored later.",
    "Write-Back Cache": "Writes data to memory only when the cache line is replaced.",
    "Write-Through Cache": "Writes data to both cache and main memory simultaneously."
    }

    selected_term = st.sidebar.selectbox("Select a term", list(terminology.keys()))
    st.sidebar.write(f"**Definition:** {terminology[selected_term]}")

    st.markdown("""
        <style>
            .reportview-container .main .block-container {
                max-width: 7in;
                padding: 1in;
                margin: auto;
            }
            .stTitle {
                font-size: 18px;
                font-weight: bold;
                text-align: center;
            }
            .stHeader {
                font-size: 13px;
                font-weight: bold;
                margin-top: 15px;
            }
            .stText {
                font-size: 11px;
                text-align: justify;
                line-height: 1.5;
            }
            b {
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)

    st.title("Virtual Machines and Memory Virtualization")

    st.header("Abstract", divider="gray")
    st.write("""
        Virtualization is a powerful technology that enables multiple **Virtual Machines (VMs)** to run on a single physical system. This paper explores the fundamental concepts of virtual machines, memory virtualization, CPU instruction handling, and cache coherence. By leveraging **VM Isolation**, **Memory Virtualization**, **Cache Coherence**, and **Instruction Set Virtualization**, modern hypervisors optimize hardware utilization while ensuring robust performance.
    """)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.header("1. Introduction")
        st.write("""
            **Virtualization** enhances efficiency, security, and scalability in modern computing environments. Multiple **Virtual Machines (VMs)** run on a single system using a **Virtual Machine Monitor (VMM) / Hypervisor**, enabling efficient resource sharing and isolation. This paper discusses the various aspects of virtualization, including **virtual memory management**, **instruction set virtualization**, and **cache coherence** in multiprocessor systems.
        """)

        st.header("2. Virtual Machine Operations")
        st.write("""
            A **Host OS vs. Guest OS** setup allows multiple **VMs** to operate within a single system. There are two primary types of hypervisors: **Type 1 Hypervisor (Bare Metal)**, which runs directly on hardware, and **Type 2 Hypervisor (Hosted)**, which runs within an existing operating system. **VM Snapshots** can save the state of a **VM** for later restoration, and **Live Migration** enables seamless movement between physical hosts.
        """)

        st.header("3. CPU and Instruction Set Virtualization")
        st.write("""
            **Trap-and-Emulate** is a technique used by the **VMM** to handle **Privileged Instructions** executed by a **Guest OS**. **Hardware-Assisted Virtualization** technologies, such as **Intel VT-x** and **AMD-V**, optimize performance and reduce emulation overhead. The **System Mode (Kernel Mode)** provides unrestricted hardware access, while **User Mode** restricts applications. **Trap Handling** ensures system security by switching execution to **System Mode** when needed.
        """)

        st.header("4. Memory Virtualization")
        st.write("""
            **Virtual Memory** allows operating systems to extend **RAM** using disk storage. **Paging** divides **virtual memory** into fixed-size units, mapped by a **Page Table** and translated by the **Memory Management Unit (MMU)**. When a **Page Fault** occurs, the **OS** retrieves the missing page from disk. **Translation Lookaside Buffer (TLB)** caching optimizes memory access, reducing **TLB Miss** rates.
        """)
    with col2:
        st.header("5. Timer Virtualization")
        st.write("""
            **Timer Virtualization** ensures proper timekeeping within **VMs**. The **VMM** manages **Virtual Timer Interrupts**, preventing **Time Drift** caused by discrepancies in virtual and physical time sources.
        """)

        st.header("6. Cache Coherence in Multiprocessor Systems")
        st.write("""
            **Cache Coherence** ensures that multiple processors have a consistent view of **memory**. The **Snooping Protocol** monitors memory changes, while an **Invalidating Snooping Protocol** ensures consistency by removing outdated cache copies. **Directory-Based Coherence** scales better in large **multiprocessor** environments.

            **Write-Through Cache** writes data to both cache and main memory, while **Write-Back Cache** only writes to memory when necessary. **Cache Migration** moves frequently accessed data closer to the relevant **processor**. **Memory Consistency** defines rules for memory update visibility.
        """)

        st.header("7. Conclusion")
        st.write("""
            **Virtualization** enhances resource efficiency and security in modern computing environments. By utilizing **VM Isolation**, **Memory Virtualization**, **Cache Coherence**, and **Instruction Set Virtualization**, **hypervisors** improve performance while ensuring robust system management. Techniques such as **Live Migration**, **TLB Optimization**, and **Trap Handling** continue to advance **virtualization** technologies, making them essential for **cloud computing** and **enterprise data centers**.
        """)

        st.header("8. References")
        st.write("""
            - [Intel VT-x and AMD-V documentation](https://www.intel.com/content/www/us/en/virtualization/virtualization-technology/intel-virtualization-technology.html)
            - [VMware ESXi and Microsoft Hyper-V official documentation](https://docs.vmware.com/en/VMware-vSphere/index.html), [Microsoft Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/hyper-v-technology-overview)
            - [Research paper on memory virtualization](https://www.usenix.org/system/files/conference/osdi14/osdi14-paper-belay.pdf)
            - [Cache Coherence Mechanisms](https://scholar.google.com/scholar?q=Cache+Coherence+for+Modern+Multicore+Processors)
            - [YouTube Video: Introduction to Virtual Machines](https://www.youtube.com/watch?v=MNxJpVymhP8)
            - [CPU and Memory Virtualization concepts explained](https://www.coursera.org/lecture/cloud-computing/virtualization-and-cloud-computing-EYbkP)
            ## Books
            - [Parallel Computer Architecture: A Hardware/Software Approach](https://www.amazon.com/Parallel-Computer-Architecture-Hardware-Software/dp/1558603433) - David Culler and Jaswinder Pal Singh  

            - [A Primer on Memory Consistency and Cache Coherence](https://www.morganclaypool.com/doi/abs/10.2200/S00254ED1V01Y201104CAC016) - Daniel J. Sorin, Mark D. Hill, and David A. Wood  

            - [The Cache Memory Book](https://www.amazon.com/Memory-Morgan-Kaufmann-Computer-Architecture/dp/0123229804) - Jim Handy  

            ## Research Papers
            - [Cache Coherence for Modern Multicore Processors](https://scholar.google.com/scholar?q=Cache+Coherence+for+Modern+Multicore+Processors) - David E. Culler and J. P. Singh  

            - [A Primer on Memory Consistency and Cache Coherence](hhttps://link.springer.com/book/10.1007/978-3-031-01764-3) - Daniel J. Sorin, Mark D. Hill, and David A. Wood  

            ## Lecture Notes
            - [Shared Memory Multiprocessors - Lecture 4](https://www.inf.ed.ac.uk/teaching/courses/pa/Notes/lecture04-multi.pdf) - University of Edinburgh  

            ## Additional Learning Resources
            - [Cloud Virtualization, Containers and APIs - Coursera Course](https://www.coursera.org/learn/cloud-virtualization-containers-api-duke?msockid=01dd85110b3065e51633908a0a8a648f)  

            - [YouTube Video: Virtual Machines explained in 15 Mins](https://www.bing.com/videos/riverview/relatedvideo?q=YouTube+Video%3a+Introduction+to+Virtual+Machines&mid=3D826722E02E67146B393D826722E02E67146B39&FORM=VIRE)  

            - [Operating System Virtualization - Master's - Coursera Course](https://www.coursera.org/learn/illinois-tech-operating-system-virtualization-mit?msockid=01dd85110b3065e51633908a0a8a648f)  

        """)

if __name__ == "__main__":
    main()