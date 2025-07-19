# Resource Allocation based on Simulated Quantum Network
## Research Foundation  
  This project extends the ideas from the research paper  
  **[Resource Allocation in Quantum Networks for Distributed Quantum Computing](https://arxiv.org/pdf/2203.05844)** by exploring additional simulations and optimization techniques.


## Problem and Proposed Solution

### Problem
Research on Quantum Internet has mainly concentrated on point-to-point communication, ideal for applications like quantum sensing and quantum key distribution (QKD). However, distributed quantum computing (DQC), which requires the connection of multiple quantum computers to perform parallel computations or solve larger problems, has not been given enough attention. This creates a demand for an advanced quantum network capable of managing end-to-end entanglement and effective resource allocation.

### Proposed Solution
The authors introduce a resource allocation approach specifically designed for DQC applications. This approach takes into account the unique needs of end-to-end entanglement and evaluates its performance through simulations. Key features and trade-offs are identified, laying the groundwork for future optimization efforts.

## Summary
The paper titled "Resource Allocation in Quantum Networks for Distributed Quantum Computing" delves into the emerging requirement for efficient resource allocation strategies in quantum networks to support distributed quantum computing (DQC). While current Quantum Internet research largely focuses on point-to-point communication (for uses such as quantum key distribution and sensing), these approaches are insufficient for the demands of DQC, which require the interconnection of several quantum computers to share resources and collaborate on complex computational tasks.  
To address this gap, the authors propose a new resource allocation method tailored to DQC needs. This strategy is crafted to manage end-to-end entanglement, which is a critical element in quantum networking. By simulating this approach, the authors identify important trade-offs, such as the balance between fidelity and capacity, which must be optimized for practical use. Additionally, the paper identifies potential areas for future exploration, including methods for purification, runtime optimization, and the integration of the strategy with lower-layer protocols.  
The research emphasizes the need to expand the Quantum Internet from basic point-to-point applications to more advanced systems capable of supporting scalable, efficient quantum computing, ultimately advancing quantum technologies.

## Key Results
1. The strategy highlights important trade-offs, such as balancing fidelity and capacity, which influence network efficiency.
2. Simulation results indicate a need for further integration with link-layer protocols and advanced techniques like purification to enhance fidelity.

## Technical Strengths and Weaknesses

### Strengths
- The paper brings a novel focus to distributed quantum computing.
- It provides a thorough simulation and evaluation of the proposed resource allocation strategy.
- It identifies key trade-offs, offering valuable insights that can guide future research.

### Weaknesses
- The paper has limited coverage of runtime optimization for large-scale networks.
- The challenges of simulations are not fully explained, leaving some uncertainties about performance aspects.
- There is insufficient focus on how the strategy can be integrated with lower-layer protocols.

## Suggestions for Future Work
1. **Incorporate Purification Techniques**: Enhance entanglement fidelity while optimizing capacity.
2. **Runtime Optimization**: Develop algorithms that allow for dynamic resource allocation during live operations.
3. **Integration with Protocol Layers**: Ensure that resource allocation works seamlessly with link and network-layer protocols.
4. **Extend Simulation Scope**: Conduct simulations using larger networks with realistic quantum device constraints to assess scalability.
