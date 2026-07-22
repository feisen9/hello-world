/**
 * 红黑树实现
 * 红黑树是一种自平衡二叉查找树，具有以下性质：
 * 1. 每个节点要么是红色，要么是黑色
 * 2. 根节点是黑色
 * 3. 每个叶子节点（NIL节点）是黑色
 * 4. 如果一个节点是红色，则它的两个子节点都是黑色
 * 5. 对每个节点，从该节点到其所有后代叶子节点的简单路径上，均包含相同数目的黑色节点
 */
public class RedBlackTree {

    // 节点颜色常量
    private static final boolean RED = true;
    private static final boolean BLACK = false;

    // 节点类
    private class Node {
        int key;
        boolean color;
        Node left;
        Node right;
        Node parent;

        Node(int key, boolean color) {
            this.key = key;
            this.color = color;
            this.left = null;
            this.right = null;
            this.parent = null;
        }
    }

    private Node root;

    public RedBlackTree() {
        root = null;
    }

    /**
     * 左旋操作
     */
    private void rotateLeft(Node node) {
        if (node == null || node.right == null) {
            return;
        }

        Node right = node.right;
        node.right = right.left;

        if (right.left != null) {
            right.left.parent = node;
        }

        right.parent = node.parent;

        if (node.parent == null) {
            root = right;
        } else if (node == node.parent.left) {
            node.parent.left = right;
        } else {
            node.parent.right = right;
        }

        right.left = node;
        node.parent = right;
    }

    /**
     * 右旋操作
     */
    private void rotateRight(Node node) {
        if (node == null || node.left == null) {
            return;
        }

        Node left = node.left;
        node.left = left.right;

        if (left.right != null) {
            left.right.parent = node;
        }

        left.parent = node.parent;

        if (node.parent == null) {
            root = left;
        } else if (node == node.parent.right) {
            node.parent.right = left;
        } else {
            node.parent.left = left;
        }

        left.right = node;
        node.parent = left;
    }

    /**
     * 插入节点
     */
    public void insert(int key) {
        Node newNode = new Node(key, RED);

        if (root == null) {
            root = newNode;
            root.color = BLACK;
            return;
        }

        Node current = root;
        Node parent = null;

        // 找到插入位置
        while (current != null) {
            parent = current;
            if (key < current.key) {
                current = current.left;
            } else if (key > current.key) {
                current = current.right;
            } else {
                // 键已存在，不插入重复键
                return;
            }
        }

        newNode.parent = parent;
        if (key < parent.key) {
            parent.left = newNode;
        } else {
            parent.right = newNode;
        }

        // 修复红黑树性质
        fixInsert(newNode);
    }

    /**
     * 修复插入后可能破坏的红黑树性质
     */
    private void fixInsert(Node node) {
        while (node != root && node.parent.color == RED) {
            Node parent = node.parent;
            Node grandParent = parent.parent;

            if (parent == grandParent.left) {
                Node uncle = grandParent.right;

                // Case 1: 叔叔节点是红色
                if (uncle != null && uncle.color == RED) {
                    grandParent.color = RED;
                    parent.color = BLACK;
                    uncle.color = BLACK;
                    node = grandParent;
                } else {
                    // Case 2: 叔叔节点是黑色，且当前节点是右子节点
                    if (node == parent.right) {
                        rotateLeft(parent);
                        node = parent;
                        parent = node.parent;
                    }

                    // Case 3: 叔叔节点是黑色，且当前节点是左子节点
                    rotateRight(grandParent);
                    boolean tempColor = parent.color;
                    parent.color = grandParent.color;
                    grandParent.color = tempColor;
                    node = parent;
                }
            } else {
                Node uncle = grandParent.left;

                // Case 1: 叔叔节点是红色
                if (uncle != null && uncle.color == RED) {
                    grandParent.color = RED;
                    parent.color = BLACK;
                    uncle.color = BLACK;
                    node = grandParent;
                } else {
                    // Case 2: 叔叔节点是黑色，且当前节点是左子节点
                    if (node == parent.left) {
                        rotateRight(parent);
                        node = parent;
                        parent = node.parent;
                    }

                    // Case 3: 叔叔节点是黑色，且当前节点是右子节点
                    rotateLeft(grandParent);
                    boolean tempColor = parent.color;
                    parent.color = grandParent.color;
                    grandParent.color = tempColor;
                    node = parent;
                }
            }
        }

        root.color = BLACK;
    }

    /**
     * 中序遍历（打印有序序列）
     */
    public void inorderTraversal() {
        inorderHelper(root);
        System.out.println();
    }

    private void inorderHelper(Node node) {
        if (node != null) {
            inorderHelper(node.left);
            System.out.print(node.key + "(" + (node.color ? "R" : "B") + ") ");
            inorderHelper(node.right);
        }
    }

    /**
     * 搜索节点
     */
    public boolean search(int key) {
        Node current = root;
        while (current != null) {
            if (key == current.key) {
                return true;
            } else if (key < current.key) {
                current = current.left;
            } else {
                current = current.right;
            }
        }
        return false;
    }

    // 测试主方法
    public static void main(String[] args) {
        RedBlackTree rbt = new RedBlackTree();

        // 插入一些数据
        int[] keys = {20, 15, 25, 10, 5, 18, 22, 28, 30, 27};
        System.out.println("插入序列: ");
        for (int key : keys) {
            rbt.insert(key);
            System.out.print(key + " ");
        }
        System.out.println("\n\n中序遍历结果 (值(颜色)):");
        rbt.inorderTraversal();

        // 搜索测试
        System.out.println("\n搜索结果:");
        int[] searchKeys = {15, 22, 100};
        for (int key : searchKeys) {
            System.out.println("搜索 " + key + ": " + (rbt.search(key) ? "找到" : "未找到"));
        }
    }
}
