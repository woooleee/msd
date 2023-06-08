first_gdf_idx    = list(gdf_normalized.index)[0] # 650(for gbd)
centroid_gdf_idx = gdf_normalized['bd_height'].idxmax()
centroid_w_idx = centroid_gdf_idx - first_gdf_idx
print(f'Centroid Building is {gdf_normalized.loc[centroid_gdf_idx].bdnm}\ngdf_idx is {centroid_gdf_idx}\nw_idx is {centroid_w_idx}')
init_w = Queen.from_dataframe(gdf_normalized)

init_gdf_idxs = list(gdf[gdf['grid_idx'].isin(gbd_init_grid_idx)].index)
init_w_idxs = [x - first_gdf_idx for x in list(init_gdf_idxs)]

cluster = init_w_idxs
prev_w_idxs = cluster

for phase in range(5):
    tba_w_idxs = []
    for w_idx in prev_w_idxs:
        tba_idxs = init_w.neighbors[w_idx]
        if len(tba_idxs) == 0:
            print('zero1!!')
            gdf_idx = w_idx + first_gdf_idx
            gdf_grid_idx = gdf.loc[gdf_idx].grid_idx
            gdf_near_grid_idx = gdf_near_idx_pair[gdf_near_idx_pair['grid_idx'] == gdf_grid_idx].near_grid_idx
            tba_idx = gdf[gdf['grid_idx'] == gdf_near_grid_idx].index - first_gdf_idx
            print(tba_idx)
        else:
            tba_w_idxs.extend(tba_idxs) # tba: to be added
    tba_w_idxs = list(set(tba_w_idxs))
    prev_w_idxs = tba_w_idxs
    assert len(tba_w_idxs) >= 1
    cluster.extend(tba_w_idxs)
    cluster = list(set(cluster))
    cluster_gdf_idxs = [x + first_gdf_idx for x in list(cluster)]
    new_gdf = gdf_normalized.loc[cluster_gdf_idxs]
    print(list(new_gdf.grid_idx.values))
    sim = within_boundary_similarity(new_gdf, SIM_CAL_COLS)
    # print('bdnms', new_gdf.bdnm.values)
    print('round', phase)
    print('sim', sim)