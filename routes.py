@bp.route('/blockchain/status')
def blockchain_status():
    """
    Endpoint to get the status of the blockchain node.
    """
    try:
        node_url = os.environ["MHDBLOCKCHAIN_NODE_URL"]
        api_key = os.environ["MHDBLOCKCHAIN_API_KEY"]
    except KeyError as e:
        return jsonify({"error": f"Missing env var: {str(e)}"}), 500
    
    try:
        response = requests.get(f"{node_url}/status", headers={"Authorization": f"Bearer {api_key}"}, timeout=5)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.Timeout:
        return jsonify({"error": "Blockchain status request timed out"}), 504
    except requests.RequestException as e:
        return jsonify({"error": "Blockchain status failed", "details": str(e)}), 502
