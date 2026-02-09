# Support Vector Machine (SVM) – Worksheet Solutions

## 1
Objective: maximize margin while minimizing classification error.  
Margin improves generalization.

## 2 (C very large)
- Small margin  
- Low training error  
- Overfitting risk high  

## 3 (C very small)
- Large margin  
- More misclassification allowed  
- Better for noisy data  

## 4
Narrow margin → high complexity → overfitting → poor generalization.

## 5
Hard-margin needs perfect separation.  
One outlier → no solution.

## 6
Uses kernel trick to map data to higher dimension where it becomes linearly separable.

## 7
RBF better than linear → data is non-linear.

## 8
(a) γ very large → complex boundary → overfitting  
(b) γ very small → smooth boundary → underfitting  

## 9
High γ memorizes noise → overfitting.

## 10
Margin = 1 / ||w||  
Large ||w|| → small margin  
Small ||w|| → large margin

## 11
Prefer Model A (larger margin → better generalization).

## 12
SVM works well in high dimensions and uses only support vectors.

## 13
Only support vectors affect the decision boundary. Distant points do not matter.

## 14
Few support vectors → efficient and faster prediction.

---

# Interview Questions

## 1
Margin maximization gives better generalization than minimizing error only.

## 2
C controls error tolerance.  
γ controls boundary complexity.  
Together manage bias–variance tradeoff.

## 3
SVM is distance-based, so scaling is necessary. Without scaling, large-value features dominate.

## 4
Not directly. Use Platt scaling or probability calibration.

## 5
Only support vectors define the hyperplane.

## 6
Use Linear SVM when:
- large dataset
- high dimension
- almost linear separation
- need faster training

## 7
Training is slow due to quadratic optimization.

## 8 Limitations
- Slow for big data
- Kernel tuning difficult
- Less interpretable
